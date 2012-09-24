from google.appengine.ext import db
from google.appengine.api import users

from bo import *


class Library(ChangeLogModel):
    model_version   = db.StringProperty(default='A')
    added_datetime  = db.DateTimeProperty(auto_now_add=True)
    added_by        = db.UserProperty(auto_current_user_add=True)
    is_deleted      = db.BooleanProperty(default=False)
    name            = db.StringProperty()
    note            = db.TextProperty()


class Group(ChangeLogModel):
    model_version   = db.StringProperty(default='A')
    added_datetime  = db.DateTimeProperty(auto_now_add=True)
    added_by        = db.UserProperty(auto_current_user_add=True)
    is_deleted      = db.BooleanProperty(default=False)
    library         = db.ReferenceProperty(Library, collection_name='groups')
    name            = db.StringProperty(default='')
    note            = db.TextProperty(default='')


class Person(ChangeLogModel):
    model_version   = db.StringProperty(default='A')
    added_datetime  = db.DateTimeProperty(auto_now_add=True)
    added_by        = db.UserProperty(auto_current_user_add=True)
    is_deleted      = db.BooleanProperty(default=False)
    libraries       = db.ListProperty(db.Key)
    user            = db.UserProperty()
    forename        = db.StringProperty(default='')
    surname         = db.StringProperty(default='')
    email           = db.StringProperty()
    idcode          = db.StringProperty(default='')
    birth_date      = db.DateProperty()
    gender          = db.StringProperty(choices=['', 'male', 'female'], default='')
    note            = db.TextProperty(default='')
    groups          = db.ListProperty(db.Key)
    type            = db.StringProperty(choices=['admin', 'staff', 'normal', 'guest'])
    activation_key  = db.StringProperty()

    @property
    def current(self):
        user = users.get_current_user()
        if user:
            return db.Query(Person).filter('user', user).get()

    @property
    def current_library(self):
        return Library().get(self.current.libraries[0])

    @property
    def libraries2(self):
        return Library().get(self.current.libraries)

    @property
    def displayname(self):
        if self.forename or self.surname:
            name = ''
            if self.forename:
                name = name + self.forename
            if self.surname:
                name = name + ' ' + self.surname
            return name
        else:
            return self.username.split('@')[0]