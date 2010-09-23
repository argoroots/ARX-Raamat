from google.appengine.ext import db
from google.appengine.ext import search


class v7download(db.Model):
    datetime    = db.DateTimeProperty(auto_now_add=True)
    type        = db.StringProperty()
    ip          = db.StringProperty()


class v7user(db.Model):
    library_id =        db.IntegerProperty(default=0)
    library_name =      db.StringProperty(default='')
    library_address =   db.StringProperty(default='')
    library_city =      db.StringProperty(default='')
    library_zip =       db.StringProperty(default='')
    library_county =    db.StringProperty(default='')
    library_phone =     db.StringProperty(default='')
    library_mail =      db.StringProperty(default='')
    contact_name =      db.StringProperty(default='')
    contact_phone =     db.StringProperty(default='')
    contact_mail =      db.StringProperty(default='')
    programm_id =       db.StringProperty(default='')
    registered_time =   db.DateTimeProperty(auto_now_add=True)
    check_lasttime =    db.DateTimeProperty()
    check_count =       db.IntegerProperty()


class v7error(db.Model):
    registered_time =   db.DateTimeProperty(auto_now_add=True)
    library_id =        db.IntegerProperty(default=0)
    library_name =      db.StringProperty(default='')
    programm_id =       db.StringProperty(default='')
    error_function  =   db.StringProperty(default='')
    error_number =      db.StringProperty(default='')
    error_text =        db.StringProperty(default='')