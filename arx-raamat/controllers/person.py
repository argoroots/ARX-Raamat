from bo import *


class Frontpage(webapp.RequestHandler):
    def get(self):
        if User().current().is_guest == True:
            View(self, '', 'person.html')
        else:
            self.redirect('/dashboard')


def main():
    Route([
             ('/person', Frontpage),
            ])


if __name__ == '__main__':
    main()