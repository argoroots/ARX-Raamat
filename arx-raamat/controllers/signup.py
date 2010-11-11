from bo import *
from database import *


class PersonData(webapp.RequestHandler):
    def get(self, id=None, key=None):

        if User().current:
            LogOut(self, '/signup/' + id + '/' + key)

        person = Person().get_by_id(int(id))

        if person and person.activation_key == key:
            View(self, '', 'signup.html', {'person': person})
        else:
            self.redirect('/')

    def post(self, id=None, key=None):

        if User().current:
            LogOut(self, '/signup/' + id + '/' + key)

        person = Person().get_by_id(int(id))

        if person and person.activation_key == key:
            person.forename = self.request.get('forename').strip()
            person.surname = self.request.get('surname').strip()
            person.email = self.request.get('email').strip()
            person.save()

            LogIn(self, '/signup2/' + id + '/' + key)
        else:
            self.redirect('/')


class JoinUser(webapp.RequestHandler):
    def get(self, id=None, key=None):

        if not User().current:
            LogOut(self, '/signup/' + id + '/' + key)
        else:
            person = Person().get_by_id(int(id))

            if person and person.activation_key == key:
                person.user = User().current
                person.activation_key = None
                person.status = 'normal'
                person.save()
                self.redirect('/')
            else:
                LogOut(self)


def main():
    Route([
             ('/signup/(.*)/(.*)', PersonData),
             ('/signup2/(.*)/(.*)', JoinUser),
            ])


if __name__ == '__main__':
    main()