from bo import *
from importers.apollo import *
from importers.lasering import *

class ApolloSearchTest(webapp.RequestHandler):
    def get(self, url):
        
        result = SearchBook(url)
        for i in result:
        	self.response.out.write('<hr />')
        	for m in i:
        		self.response.out.write(m + '=>' + i[m] + '<br />')

class LaseringTest(webapp.RequestHandler):
    def get(self, url):
        result = GetItemByID(url)
        for n in result:
        	self.response.out.write(n + ' => ' + result[n] + '<br />')

class ApolloBookTest(webapp.RequestHandler):
    def get(self, url):
        result = GetBookByID(url)
        for n in result:
        	self.response.out.write(n + ' => ' + result[n] + '<br />')


def main():
    Route([
             ('/test/apollo/search/(.*)', ApolloSearchTest),
             ('/test/apollo/(.*)', ApolloBookTest),
             ('/test/lasering/(.*)', LaseringTest),
            ])


if __name__ == '__main__':
    main()