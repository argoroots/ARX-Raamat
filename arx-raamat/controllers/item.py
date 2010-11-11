from urllib import unquote

from bo import *
from database import *
from importers import *


class AddNewItem(webapp.RequestHandler):
    def get(self):

        if self.request.get('item_id'):
            book = EsterGetByID(self.request.get('item_id'))

            item = db.Query(Item).filter('original_id', book['id']).get()
            if item:
                libs = item.libraries
                libs.append(Person().current.library.key())
                libs = list(set(libs))
                item.libraries = libs
            else:
                tagkeys = []
                for tag, values in book.iteritems():
                    if tag not in ['authors', 'id']:
                        for value in values:
                            tagkeys.append(AddTag(tag, value))
                    if tag == 'authors':
                        for value in values:
                            tagkeys.append(AddTag(value['role'], value['name'], value['date']))

                item = Item()
                item.added_by = str(Person().current.key())
                item.original_id = book['id']
                item.title = book['title'][0]
                item.libraries.append(Person().current.library.key())
                item.tags = tagkeys
                item.put()

            #self.redirect('/item/edit/' + str(item.key().id()))
            self.redirect('/catalog/author')


class ImageByIsbn(webapp.RequestHandler):
    def get(self, isbn):
        isbnlist = unquote(isbn).decode('utf8').split(' ')
        #self.response.out.write(ImageByISBN(isbnlist[0]))
        self.redirect(ImageByISBN(isbnlist[0]))


class SearchForNew(webapp.RequestHandler):
    def post(self):
        string = self.request.get('search_text')
        result = EsterSearch(string, 30)
        #self.response.out.write(result)
        View(self, '', 'item_searchfornew.html', {'items': result})


def main():
    Route([
             ('/item/add', AddNewItem),
             ('/item/searchfornew', SearchForNew),
             (r'/item/imagebyisbn/(.*)', ImageByIsbn),
            ])


if __name__ == '__main__':
    main()