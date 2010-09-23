from bo import *


class Frontpage(webapp.RequestHandler):
    def get(self):
        #self.redirect('/v7')
        View(self, '', 'frontpage.html')


def main():
    Route([
             ('/', Frontpage),
            ])


if __name__ == '__main__':
    main()