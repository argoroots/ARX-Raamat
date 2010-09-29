from bo import *
from importers.apollo import *


class ApolloTest(webapp.RequestHandler):
    def get(self, url):
        #url = '0817496'
        result = GetBookByID(url)
        self.response.out.write(result)


def main():
    Route([
             ('/test/apollo/(.*)', ApolloTest),
            ])


if __name__ == '__main__':
    main()