from bo import *
from database.person import *


class Frontpage(boRequestHandler):
    def get(self):
        if Person().current:
            self.view('', 'frontpage.html')
        else:
            self.redirect('/v7')


def main():
    Route([
             ('/', Frontpage),
            ])


if __name__ == '__main__':
    main()