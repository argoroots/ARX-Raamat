from bo import *
from database.item import *


class ShowTags(boRequestHandler):
    def get(self, url):
        tagtype_name = url.strip('/')
        if not tagtype_name:
            self.redirect('/catalog/author')
            return

        tagtype = TagType().get_by_name(tagtype_name)
        tags = Tag().get_by_type_name(tagtype_name)

        nav = []
        for tt in TagType().get_public():
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

        tagtype = TagType().get_by_name(tagtype_name)
        tag = Tag().get_by_id(int(id))

        items = db.Query(Item)
        items.filter('tags', tag.key())
        items.order('title')
        items.fetch(1000)

        nav = []
        for tt in TagType().get_public():
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