from google.appengine.api import users
from google.appengine.api import images
import urllib

from bo import *


class Activate(webapp.RequestHandler):

    def get(self, email = None, key = None):

        email = urllib.unquote(email).decode('utf8')
        key = urllib.unquote(key).decode('utf8')

        if email and key and users.get_current_user().federated_identity():
            u = db.Query(User).filter('email =', email).filter('activation_key =', key).get()

        if u:
            ids = u.identities
            ids.append(users.get_current_user().federated_identity())
            u.identities = list(set(ids))
            u.activation_key = None
            u.save()

        self.redirect('/')


class Preferences(webapp.RequestHandler):

    def get(self):
        p = Person.current()
        form = UserPreferencesForm(self.request.POST, p)
        form.avatar.data = None

        View(self, 'user_preferences', 'user_preferences.html', { 'form': form, 'person': p })

    def post(self):
        form = UserPreferencesForm(self.request.POST)

        if form.validate():
            p = boUser()
            p.forename = form.forename.data
            p.surname = form.surname.data
            p.language = form.language.data
            if self.request.get("avatar"):
                p.avatar = db.Blob(boRescale(self.request.get("avatar"), 40, 40))
            p.save()

        self.redirect('')


def main():
    Route([
        (r'/user/activate/(.*)/(.*)', Activate),
        (r'/user/preferences', Preferences),
    ])


if __name__ == '__main__':
    main()