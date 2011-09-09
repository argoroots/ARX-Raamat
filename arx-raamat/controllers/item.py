from urllib import unquote

from bo import *
from database.person import *
from database.item import *
from importers import *


class ShowItem(boRequestHandler):
    def get(self, id, page = ''):

        if page not in ['', 'copies', 'lending']:
            page = ''

        tagtypes = TagType().GetPublic()
        item = Item().get_by_id(int(id))

        nav = [
            {'url': '/item/' + str(id), 'name': Translate('item_info'), 'selected': (page == '')},
            {'url': '/item/' + str(id) + '/copies', 'name': Translate('item_copies'), 'selected': (page == 'copies')},
            {'url': '/item/' + str(id) + '/lending', 'name': Translate('lending'), 'selected': (page == 'lending')},
        ]

        self.view(item.displayname, 'catalog/catalog.html', {
            'image': item.image,
            'nav': nav,
            'item': item,
        })


class AddNewItem(boRequestHandler):
    def post(self):
        item_id = self.request.get('item_id')
        if item_id:
            book = EsterGetByID(item_id)
            item = db.Query(Item).filter('original_id', book['id']).get()

            if not item:
                item = Item()
                item.original_from = 'ester'
                item.original_id = book['id']
                item.title = book['title'][0]['value']

                for tag, values in book.iteritems():
                    if tag != 'id':
                        for value in values:
                            item.AddTag(type_name=tag, value=value['value'], note=value['note'])

            item.libraries = AddToList(Person().current_library.key(), item.libraries)
            item.put()

            self.echo('/item/' + str(item.key().id()))


class ImageByIsbn(boRequestHandler):
    def get(self, url):
        isbn = unquote(url).decode('utf8').split(' ')[0]

        if not isbn:
            self.redirect('/images/blank.png')
            return

        imageurl = Cache().get('image_isbn' + isbn)
        if imageurl:
            self.redirect(imageurl)
            return

        imageurl = ImageByISBN(isbn)
        if imageurl:
            Cache().set('image_isbn_' + isbn, imageurl)
            self.redirect(imageurl)
            return

        self.redirect('/images/blank.png')


class SearchForNew(boRequestHandler):
    def post(self):
        string = self.request.get('search_text')
        result = EsterSearch(string)
        self.view('', 'item/new_search_list.html', {'items': result})


def main():
    Route([
             ('/item/add', AddNewItem),
             ('/item/searchfornew', SearchForNew),
             (r'/item/imagebyisbn/(.*)', ImageByIsbn),
             (r'/item/(.*)/(.*)', ShowItem),
             (r'/item/(.*)', ShowItem),
            ])


if __name__ == '__main__':
    main()