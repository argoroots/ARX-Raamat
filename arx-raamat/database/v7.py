from google.appengine.ext import db
from google.appengine.ext import search


class v7download(db.Model):
    datetime    = db.DateTimeProperty(auto_now_add=True)
    type        = db.StringProperty()
    ip          = db.StringProperty()