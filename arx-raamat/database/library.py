from google.appengine.ext import db


class Library(db.Model):
    date_added  = db.DateTimeProperty(auto_now_add=True)
    name        = db.StringProperty()
    note        = db.TextProperty()