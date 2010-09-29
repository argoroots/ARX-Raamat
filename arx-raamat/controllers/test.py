from bo import *
from importers.apollo import *

class ApolloSearchTest(webapp.RequestHandler):
    def get(self, url):
        #url = '0817496'
        result = SearchBook(url)
        self.response.out.write(result)


class ApolloBookTest(webapp.RequestHandler):
    def get(self, url):
        result = GetBookByID(url)
        self.response.out.write(result)


def main():
    Route([
             ('/test/apollo/search/(.*)', ApolloSearchTest),
             ('/test/apollo/(.*)', ApolloBookTest),
            ])


if __name__ == '__main__':
    main()