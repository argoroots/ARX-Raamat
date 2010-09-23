from bo import *


class Frontpage(webapp.RequestHandler):
    def get(self):
        View(self, '', 'catalog.html')


def main():
    Route([
             ('/catalog', Frontpage),
            ])


if __name__ == '__main__':
    main()