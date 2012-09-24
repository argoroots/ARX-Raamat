from google.appengine.api import users

from bo import *
from database.person import *


class PersonData(boRequestHandler):
    def get(self, url=None):
        id = url.split('.')[0]
        key = url.split('.')[1]

        if users.get_current_user():
            self.logout('/signup/' + url)

        person = Person().get_by_id(int(id))

        if person and person.activation_key == key:
            self.view('', 'signup.html', {'person': person})
        else:
            self.redirect('/')

    def post(self, url=None):
        id = url.split('.')[0]
        key = url.split('.')[1]

        if users.get_current_user():
            self.logout('/signup/' + url)

        person = Person().get_by_id(int(id))

        if person and person.activation_key == key:
            person.forename = self.request.get('forename').strip()
            person.surname = self.request.get('surname').strip()
            person.put()

            self.login('/signup2/' + url)
        else:
            self.redirect('/')


class JoinUser(boRequestHandler):
    def get(self, url=None):
        id = url.split('.')[0]
        key = url.split('.')[1]

        user = users.get_current_user()
        if not user:
            self.logout('/signup/' + url)
        else:
            person = Person().get_by_id(int(id))
            if person and person.activation_key == key:
                person.user = user
                person.activation_key = None
                person.put()
                self.redirect('/')
            else:
                self.logout()


def main():
    Route([
             ('/signup/(.*)', PersonData),
             ('/signup2/(.*)', JoinUser),
            ])


if __name__ == '__main__':
    main()