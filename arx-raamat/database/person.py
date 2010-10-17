from google.appengine.ext import db
from google.appengine.ext import search

from bo.user import *
from database import *


class Person(search.SearchableModel):
    library         = db.ReferenceProperty(Library, collection_name='persons')
    forename        = db.StringProperty(default='')
    surname         = db.StringProperty(default='')
    email           = db.StringProperty()
    idcode          = db.StringProperty(default='')
    birth_date      = db.DateProperty()
    gender          = db.StringProperty()
    note            = db.TextProperty(default='')
    activation_key  = db.StringProperty()
    user            = db.ReferenceProperty(User, collection_name='persons')

    def current(self):
        return db.Query(Person).filter('user =', User().current()).get()


class Contact(db.Model):
    person      = db.ReferenceProperty(Person, collection_name='contacts')
    type        = db.StringProperty()
    value       = db.StringProperty()


class Group(db.Model):
    name        = db.StringProperty()
    note        = db.TextProperty()


class PersonGroup(db.Model):
    person      = db.ReferenceProperty(Person, collection_name='groups')
    group       = db.ReferenceProperty(Group, collection_name='persons')