from google.appengine.ext import db
from google.appengine.ext import search
from google.appengine.api import users

from bo.user import *
from bo.settings import *


class User(db.Model):
    create_date     = db.DateTimeProperty(auto_now_add=True)
    email           = db.StringProperty()
    password        = db.StringProperty()
    identities      = db.StringListProperty()
    activation_key  = db.StringProperty()
    language        = db.StringProperty()
    last_login_date = db.DateTimeProperty()

    def current(self):
        u = None
        user = users.get_current_user()

        if user and user.federated_identity():
            u = db.Query(User).filter('identities =', user.federated_identity()).get()
            if u and not u.language:
                u.language = SYSTEM_LANGUAGE
                u.save()

        if u:
            u.is_guest = False
        else:
            u = User()
            u.is_guest = True
            u.name = GUEST_NAME
            u.email = GUEST_EMAIL
            u.language = SYSTEM_LANGUAGE

        return u