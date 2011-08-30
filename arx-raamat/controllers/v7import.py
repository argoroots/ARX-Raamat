import urllib
import base64
import chardet
import codecs

from bo import *
from database.v7 import *


class ImportItem(boRequestHandler):
    def get(self):

        encoding = self.request.get('e')
        encoding2 = self.request.get('e2')

        self.header('Content-Type', 'text/plain; charset=UTF-8')
        for i in db.Query(v7item).filter('encoding', encoding).fetch(1000):
            if encoding2:
                self.echo(unicode(base64.b64decode(i.base64), encoding2))
            else:
                self.echo(i.title)

    def post(self):
        b64 = self.request.get('string').replace(' ', '+')

        item = db.Query(Item).filter('original_id', book['id']).get()
        if not item:
            item = Item()
            item.original_from = 'v7'
            item.original_id = book['id']
            item.marc21 = book['marc21']
            item.title = book['title'][0]

            for tag, values in book.iteritems():
                if tag not in ['id', 'authors', 'marc21']:
                    for value in values:
                        item.add_tag(type_name=tag, value=value)
                if tag == 'authors':
                    for value in values:
                        item.add_tag(type_name=value['role'], value=value['name'], note=value['date'])

        item.libraries = AddToList(Person().current_library.key(), item.libraries)
        item.put()

        self.echo('/item/' + str(item.key().id()))

        self.echo('OK', False)


def ConvertBase64String(string):
    string = base64.b64decode(string).replace(' ', '+')
    encoding = chardet.detect(string)['encoding']
    if encoding in ['ISO-8859-2', 'ascii', 'windows-1252', 'windows-1255']:
        encoding = 'ISO-8859-2'
    if encoding in ['windows-1251', 'MacCyrillic']:
        encoding = 'windows-1251'
    if not encoding:
        encoding = 'windows-1251'
    return unicode(string, encoding).replace('\n', ' ')


def main():
    Route([
        ('/v7import', ImportItem),
    ])


if __name__ == '__main__':
    main()