from bo import *
from database.item import *


class ShowTags(boRequestHandler):
    def get(self, url):
        tagtype_name = url.strip('/')
        if not tagtype_name:
            self.redirect('/catalog/author')
            return

        tagtypes = TagType().get_public()
        tagtype = TagType().get_by_name(tagtype_name)
        tags = Tag().get_by_type_name(tagtype_name)

        self.view(tagtype.displayname, 'catalog/catalog.html', {
            'tagtypes': tagtypes,
            'tagtype': tagtype,
            'tags': tags,
        })


class ShowItems(boRequestHandler):
    def get(self, tagtype_name, id):

        tagtypes = TagType().get_public()
        tagtype = TagType().get_by_name(tagtype_name)
        tag = Tag().get_by_id(int(id))

        items = db.Query(Item)
        items.filter('tags', tag.key())
        items.order('title')
        items.fetch(1000)

        self.view(tagtype.displayname + ' : ' + tag.value, 'catalog/catalog.html', {
            'tagtypes': tagtypes,
            'tagtype': tagtype,
            'items': items,
        })


def main():
    Route([
             (r'/catalog/(.*)/(.*)', ShowItems),
             (r'/catalog(.*)', ShowTags),
            ])


if __name__ == '__main__':
    main()