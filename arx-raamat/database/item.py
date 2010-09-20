from google.appengine.ext import db
from google.appengine.ext import search

from database import *
from bo.user import *


class Library(db.Model):
    name        = db.StringProperty()
    note        = db.TextProperty()


class ItemType(db.Model):
    name        = db.StringProperty()
    note        = db.TextProperty()


class Item(db.Model):
    date_added  = db.DateTimeProperty()
    library     = db.ReferenceProperty(Library, collection_name='items')
    item_type   = db.ReferenceProperty(ItemType, collection_name='items')
    name        = db.StringProperty()
    note        = db.TextProperty()


class TagType(db.Model):
    ordinar     = db.IntegerProperty(default=0)
    name        = db.StringProperty()
    type        = db.StringProperty()


class Tag(db.Model):
    tag_type   = db.ReferenceProperty(ItemType, collection_name='tags')

