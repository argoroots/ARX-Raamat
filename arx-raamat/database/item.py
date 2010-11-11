from google.appengine.ext import db
from google.appengine.ext import search

from bo import *
from database import *


class Item(db.Model):
    date_added  = db.DateTimeProperty(auto_now_add=True)
    added_by    = db.StringProperty()
    original_id = db.StringProperty()
    libraries   = db.ListProperty(db.Key)
    title       = db.StringProperty()
    tags        = db.ListProperty(db.Key)
    update      = db.StringProperty(default='a')

    @property
    def tag(self):
        result = []
        for t in db.Query(Tag).filter('__key__ IN', self.tags).fetch(1000):
            result.append({
                'key': t.key(),
                'id': t.key().id(),
                'type': t.type,
                'label': Translate('type'),
                'value': t.value,
                'note': t.note
            })
        return result



class TagType(db.Model):
    date_added  = db.DateTimeProperty(auto_now_add=True)
    ordinar     = db.IntegerProperty(default=0)
    name        = db.StringProperty()
    type        = db.StringProperty()
    is_public   = db.BooleanProperty(default=False)
    update      = db.StringProperty(default='a')


class Tag(search.SearchableModel):
    date_added  = db.DateTimeProperty(auto_now_add=True)
    added_by    = db.StringProperty()
    type        = db.StringProperty()
    value       = db.StringProperty()
    note        = db.StringProperty()
    value_text  = db.StringProperty()
    update      = db.StringProperty(default='a')


def AddTagType(name):
    if not db.Query(TagType).filter('name', name).get():
        tt = TagType()
        tt.name = name
        tt.type = 'string'
        tt.put()

def GetTagTypes():
    result = []
    for type in db.Query(TagType).filter('is_public', True).order('name').fetch(100):
        result.append({
            'key': type.key(),
            'id': type.key().id(),
            'name': type.name,
            'label': Translate('tagtype_' + type.name)
        })
    return result

def AddTag(type, value, note=None):
    AddTagType(type)
    t = db.Query(Tag).filter('type', type).filter('value', value).get()
    if not t:
        t = Tag()
        t.type = type
        t.value = value
        t.note = note
        t.save()

    return t.key()
