from google.appengine.ext import db
from google.appengine.ext import search

from bo.user import *
from database import *


class Person(search.SearchableModel):
    date_added      = db.DateTimeProperty(auto_now_add=True)
    added_by        = db.StringProperty()
    library         = db.ReferenceProperty(Library, collection_name='persons')
    forename        = db.StringProperty(default='')
    surname         = db.StringProperty(default='')
    email           = db.StringProperty()
    idcode          = db.StringProperty(default='')
    birth_date      = db.DateProperty()
    gender          = db.StringProperty(choices=['male', 'female'])
    note            = db.TextProperty(default='')
    groups          = db.ListProperty(db.Key)
    type            = db.StringProperty(choices=['admin', 'staff', 'normal'], default='normal')
    status          = db.StringProperty(choices=['new', 'normal'], default='normal')
    activation_key  = db.StringProperty()
    user            = db.ReferenceProperty(User, collection_name='persons')

    @property
    def current(self):
        return db.Query(Person).filter('user =', User().current).get()


class Contact(db.Model):
    date_added  = db.DateTimeProperty(auto_now_add=True)
    person      = db.ReferenceProperty(Person, collection_name='contacts')
    type        = db.StringProperty()
    value       = db.StringProperty(default='')


class Group(db.Model):
    date_added  = db.DateTimeProperty(auto_now_add=True)
    library     = db.ReferenceProperty(Library, collection_name='groups')
    name        = db.StringProperty(default='')
    note        = db.TextProperty(default='')