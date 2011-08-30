from google.appengine.ext import db

from bo import *
from database.person import *


class Item(ChangeLogModel):
    added_datetime  = db.DateTimeProperty(auto_now_add=True)
    added_by        = db.UserProperty(auto_current_user_add=True)
    libraries       = db.ListProperty(db.Key)
    original_from   = db.StringProperty(choices=['v7', 'ester'])
    original_id     = db.StringProperty()
    title           = db.StringProperty()
    tags            = db.ListProperty(db.Key)
    marc21          = db.TextProperty()
    model_version   = db.StringProperty(default='A')

    def add_tag(self, type_key=None, type_name=None, value = '', note=None):
        if type_key:
            tagtype = TagType().get(type_key)
        if type_name:
            tagtype = db.Query(TagType).filter('name', type_name).get()

        if not tagtype:
            tagtype = TagType()
            tagtype.name = type_name
        tagtype.libraries = AddToList(Person().current_library.key(), tagtype.libraries)
        tagtype.put()

        tag = db.Query(Tag).filter('tagtype', tagtype).filter('value', value).get()
        if not tag:
            tag = Tag()
            tag.tagtype = tagtype
            tag.value = value
            tag.note = note
        tag.libraries = AddToList(Person().current_library.key(), tag.libraries)
        tag.put()

        self.tags = AddToList(tag.key(), self.tags)

    @property
    def displayname(self):
        tags = self.tag
        if 'number' in tags:
            return self.title + ' ' + tags['number'][0]
        else:
            return self.title

    @property
    def tag(self):
        cache_key = 'item_tags_' + str(Person().current_library.key()) + '_' + str(self.key())
        tags = Cache().get(cache_key)
        if not tags:
            tags = {}
            for t in Tag.get(self.tags):
                if t:
                    tagtype = t.tagtype
                    if tagtype.name not in tags:
                        tags[tagtype.name] = []
                    tags[tagtype.name].append(t.value)
            Cache().set(cache_key, tags)
        return tags

    @property
    def tags2(self):
        return Tag.get(self.tags)

    @property
    def tags3(self):
        result = []
        for t in Tag.get(self.tags):
            if t:
                tagtype = t.tagtype
                result.append({
                    'key': t.key(),
                    'id': t.key().id(),
                    'tagtype_key':  str(tagtype.key()),
                    'tagtype_id': tagtype.key().id(),
                    'tagtype_ordinar': tagtype.ordinar,
                    'tagtype_displayname': tagtype.displayname,
                    'tagtype_url': tagtype.url,
                    'tagtype_is_visible': tagtype.is_visible,
                    'displayname': t.displayname,
                    'value': t.value,
                    'note': t.note
                })
        return result


class TagType(ChangeLogModel):
    added_datetime  = db.DateTimeProperty(auto_now_add=True)
    added_by        = db.UserProperty(auto_current_user_add=True)
    libraries       = db.ListProperty(db.Key)
    ordinar         = db.IntegerProperty(default=9999)
    name            = db.StringProperty()
    name_estonian   = db.StringProperty()
    name_english    = db.StringProperty()
    name_russian    = db.StringProperty()
    type            = db.StringProperty(choices=['string', 'lower', 'upper'], default='string')
    url             = db.StringProperty()
    is_visible      = db.BooleanProperty(default=False)
    model_version   = db.StringProperty(default='A')

    @property
    def displayname(self):
        name = getattr(self, 'name_' + UserPreferences().current.language)
        if name:
            return name
        else:
            return self.name

    def get_by_name(self, name):
        return db.Query(TagType).filter('name', name).get()

    def get_public(self):
        #return db.Query(TagType).filter('url >', '').fetch(1000)
        return db.Query(TagType).fetch(1000)


class Tag(ChangeLogModel):
    added_datetime  = db.DateTimeProperty(auto_now_add=True)
    added_by        = db.UserProperty(auto_current_user_add=True)
    libraries       = db.ListProperty(db.Key)
    tagtype         = db.ReferenceProperty(TagType, collection_name='tags')
    value           = db.StringProperty()
    note            = db.StringProperty()
    model_version   = db.StringProperty(default='A')

    @property
    def displayname(self):
        if self.tagtype.type == 'lower':
            return self.value.lower()
        if self.tagtype.type == 'upper':
            return self.value.upper()
        return self.value

    def get_by_type_name(self, type_name):
        tagtype_key = db.Query(TagType, keys_only=True).filter('name', type_name).get()
        return db.Query(Tag).filter('tagtype', tagtype_key).fetch(1000)