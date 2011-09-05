# -*- coding: windows-1251 -*-

from google.appengine.api import memcache
from urllib import unquote
import urllib

import chardet

from bo import *
from database.item import *
from importers.ester import *
from importers.apollo import *
from importers.rahvaraamat import *
from importers.raamatukoi import *
from importers.googlebooks import *
from importers.amazon import *


class AmazonSearchTest(webapp.RequestHandler):
    def get(self, url):
        keywords = unquote(url).decode('utf8').strip('/')

        result = SearchBook(keywords)
        strng = ''
        for item in result:
            for i in item:
            	strng = strng + i + ' => ' + item[i] + '<br />'
            strng = strng + '<hr />'
        self.response.out.write(strng)


# N.B! Some values can be None or a list; then the test function will fail
class AmazonTest(webapp.RequestHandler):
    def get(self, url):
        keywords = unquote(url).decode('utf8').strip('/')

        result = GetBook(keywords)
        strng = ''
        for item in result:

            strng = strng + item + ' => ' + result[item] + '<br />'

        self.response.out.write(strng)


class EsterGet(webapp.RequestHandler):
    def get(self, id):

        result = EsterGetByID(id)

        self.response.out.write(str(result))


class Search(webapp.RequestHandler):
    def get(self, string):

        result = EsterSearch(string)

        self.response.out.write(str(result))
        return

        self.response.out.write('<pre>')
        if result:
            for row in result:
                for tag, value in row.iteritems():
                    if tag != 'id1':
                        self.response.out.write(tag + ' = ' + str(value) + '\n')

                self.response.out.write('\n')
        self.response.out.write('</pre>')


class Scan(webapp.RequestHandler):
    def get(self, code):

        book = None
        picture = None

        if code:
            result = EsterSearch(code, 1)
            if result:
                book = result[0]
            picture = ShowImage(code)

        View(self, '', 'scan.html', {
            'book': book,
            'picture': picture,
            'code': code
        })


def ShowImage(isbn):
    result = None
    result = RahvaraamatImageByISBN(isbn)
    if not result:
        result = RaamatukoiImageByISBN(isbn)
        if not result:
            result = GoogleImageByISBN(isbn)
    return result


class TagTypeUpdate(webapp.RequestHandler):
    def get(self):
        for tt in TagType().all():
            tt.is_visible = True
            tt.put()


def main():
    Route([
             (r'/test/get/(.*)', EsterGet),
             (r'/test/search/(.*)', Search),
             (r'/test/scan/(.*)', Scan),
             ('/test/amazon/search/(.*)', AmazonSearchTest),
             ('/test/amazon/(.*)', AmazonTest),
             ('/test/ttu', TagTypeUpdate),
            ])


if __name__ == '__main__':
    main()