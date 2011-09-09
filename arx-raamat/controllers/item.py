from urllib import unquote

from bo import *
from database.person import *
from database.item import *
from importers import *


class ShowItem(boRequestHandler):
    def get(self, id):
        tagtypes = TagType().GetPublic()
        item = Item().get_by_id(int(id))

        nav = [
            {'url': '/item/' + str(id), 'name': Translate('item_info'), 'selected': True},
            {'url': '/item/' + str(id) + '/copies', 'name': Translate('item_copies')},
            #{'url': '/item/' + str(id) + '/lending', 'name': Translate('lending')},
        ]

        self.view(item.displayname, 'catalog/catalog.html', {
            'image': item.image,
            'nav': nav,
            'item': item,
        })


class ShowCopies(boRequestHandler):
    def get(self, id):
        tagtypes = TagType().GetPublic()
        item = Item().get_by_id(int(id))
        copies = db.Query(Copy).filter('item', item).filter('library', Person().current_library.key())

        nav = [
            {'url': '/item/' + str(id), 'name': Translate('item_info')},
            {'url': '/item/' + str(id) + '/copies', 'name': Translate('item_copies'), 'selected': True},
            #{'url': '/item/' + str(id) + '/lending', 'name': Translate('lending')},
        ]

        self.view(item.displayname, 'catalog/catalog.html', {
            'image': item.image,
            'nav': nav,
            'copies': copies,
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

            copy = db.Query(Copy, keys_only=True).filter('Item', item).filter('Library', Person().current_library.key()).get()
            if not copy:
                copy = Copy()
                copy.library = Person().current_library.key()
                copy.item = item
                copy.put()
            
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
             (r'/item/(.*)/copies', ShowCopies),
             (r'/item/(.*)', ShowItem),
            ])


if __name__ == '__main__':
    main()