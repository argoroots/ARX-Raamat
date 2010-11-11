from bo import *
from database import *


class Frontpage(webapp.RequestHandler):
    def get(self, url):

        tagtype = url.strip('/')

        if not tagtype:
            self.redirect('/catalog/author')

        tags = db.Query(Tag).filter('type', tagtype).order('value').fetch(1000)

        View(self, 'tagtype_' + tagtype, 'catalog.html', {
            'tagtypes': GetTagTypes(),
            'tags': tags,
            'selected_type': tagtype,
        })


class ShowItems(webapp.RequestHandler):
    def get(self, tagtype, id):

        tag = Tag().get_by_id(int(id))

        items = db.Query(Item).filter('tags', tag.key()).order('title').fetch(1000)

        View(self, Translate('tagtype_' + tagtype) + ' : ' + tag.value, 'item_list.html', {
            'tagtypes': GetTagTypes(),
            'items': items,
            'selected_type': tagtype,
        })


def main():
    Route([
             (r'/catalog/(.*)/(.*)', ShowItems),
             (r'/catalog(.*)', Frontpage),
            ])


if __name__ == '__main__':
    main()