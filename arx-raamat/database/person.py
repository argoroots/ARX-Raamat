from google.appengine.ext import db
from google.appengine.ext import search

from database import *
from bo.user import *


class Person(search.SearchableModel):
    forename    = db.StringProperty()
    surname     = db.StringProperty()
    idcode      = db.StringProperty()
    birth_date  = db.DateProperty()
    gender      = db.StringProperty()
    note        = db.TextProperty()
    user        = db.ReferenceProperty(User, collection_name='person')

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