from bo import *


class Frontpage(webapp.RequestHandler):
    def get(self):
        View(self, '', 'person.html')


def main():
    Route([
             ('/person', Frontpage),
            ])


if __name__ == '__main__':
    main()