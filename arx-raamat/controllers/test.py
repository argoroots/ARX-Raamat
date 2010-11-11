from google.appengine.api import memcache
from urllib import unquote

from bo import *
from importers.ester import *
from importers.apollo import *
from importers.rahvaraamat import *
from importers.raamatukoi import *
from importers.googlebooks import *
from importers.lasering import *
from importers.amazon import *


class AmazonSearchTest(webapp.RequestHandler):
    def get(self, url):
        keywords = unquote(url).decode('utf8').strip('/')

        result = AmazonBookSearch(keywords)

        self.response.headers['Content-Type'] = 'text/xml'
        self.response.out.write(result)


class LaseringTest(webapp.RequestHandler):
    def get(self, url):
        result = GetItemByID(url)
        for n in result:
        	self.response.out.write(n + ' => ' + result[n] + '<br />')


class Search(webapp.RequestHandler):
    def get(self, string):

        result = EsterSearch(string, 30)

        #self.response.out.write(result)

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


def main():
    Route([
             (r'/test/search/(.*)', Search),
             (r'/test/scan/(.*)', Scan),
             ('/test/lasering/(.*)', LaseringTest),
             ('/test/amazon/(.*)', AmazonSearchTest),
            ])


if __name__ == '__main__':
    main()