from bo import *


class ShowPreferences(webapp.RequestHandler):
    def get(self):
        View(self, 'preferences', 'preferences.html', {
            'user': User().current,
        })

    def post(self):
        User().set_language(self.request.get('language'))


def main():
    Route([
             ('/preferences', ShowPreferences),
            ])


if __name__ == '__main__':
    main()