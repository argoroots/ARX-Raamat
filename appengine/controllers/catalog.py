from bo import *
from database.item import *


class ShowTags(boRequestHandler):
    def get(self, tagtype_name):
        tagtype_name = tagtype_name.strip('/')
        if not tagtype_name:
            self.redirect('/catalog/author')
            return

        tagtype = TagType().GetByName(tagtype_name)
        tags = Tag().GetByTypeName(tagtype_name)

        nav = []
        for tt in TagType().GetPublic():
            nav.append({
                'url': '/catalog/' + tt.name,
                'name': tt.displayname,
                'selected': (tt.name == tagtype.name)
            })

        self.view(tagtype.displayname, 'catalog/catalog.html', {
            'image': '/images/Catalog_100.png',
            'nav': sorted(nav, key=lambda k: k['name']),
            'tagtype': tagtype,
            'tags': tags,
        })


class ShowItems(boRequestHandler):
    def get(self, tagtype_name, id):

        tagtype = TagType().GetByName(tagtype_name)
        tag = Tag().get_by_id(int(id))

        items = db.Query(Item)
        items.filter('libraries', Person().current_library.key())
        items.filter('tags', tag.key())
        items.order('title')
        items.fetch(1000)

        nav = []
        for tt in TagType().GetPublic():
            nav.append({
                'url': '/catalog/' + tt.name,
                'name': tt.displayname,
                'selected': (tt.name == tagtype.name)
            })

        self.view(tagtype.displayname + ' : ' + tag.value, 'catalog/catalog.html', {
            'image': '/images/Catalog_100.png',
            'nav': sorted(nav, key=lambda k: k['name']),
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