import urllib
import hashlib
import time
from google.appengine.api import urlfetch
from django.utils import simplejson

from bo import *
from database.person import *
from database.item import *


class ShowAdmin(boRequestHandler):
    def get(self):
        l = db.Query(Library).order('name').fetch(1000)
        self.view('', 'admin.html', {
            'libraries': l
        })


class AddLibrary(boRequestHandler):
    def post(self):
        name = self.request.get('library').strip('')
        l = db.Query(Library).filter('name', name).get()
        if not l:
            l = Library()
            l.name = name
            l.put()
        self.redirect('/admin')


class SendInvites(boRequestHandler):
    def post(self):
        emails = self.request.get('emails')
        if emails:
            for email in StrToList(emails):

                p = db.Query(Person).filter('email', email).get()
                if not p:
                    p = Person()
                    p.email = email.lower()
                    p.type = 'admin'
                    p.put()
                p.libraries = AddToList(db.Key(self.request.get('library')), p.libraries)
                p.activation_key = hashlib.md5(str(time.time()) + email).hexdigest()[0:len(str(p.key().id()))].upper()
                p.put()

                link = SYSTEM_URL + '/signup/' + str(p.key().id()) + '.' + p.activation_key

                SendMail(
                    to = email,
                    subject = Translate('invitation_subject'),
                    message = Translate('invitation_email') % {'inviter': Person().current.displayname, 'link': link}
                )
        self.redirect('/admin')


class TranslateAll(boRequestHandler):
    def get(self, from_lang, to_lang):

        languagecodes = {
            'et': 'estonian',
            'en': 'english',
            'ru': 'russian',
        }
        api_key = 'AIzaSyDeBz3bFbw2mdOkZwi3cRpjyWqeBjOX4IY'
        translations = {}

        if from_lang in languagecodes:
            l = __import__('translations.' + languagecodes[from_lang], globals(), locals(), ['translation'], -1)

            for key, value in l.translation().iteritems():
                url = 'https://www.googleapis.com/language/translate/v2?format=html&key=' + api_key + '&q=' + urllib.quote(value) + '&source=' + from_lang + '&target=' + to_lang
                json = simplejson.loads(urlfetch.fetch(url, deadline=10).content)
                if 'data' in json:
                    translations[key] = json['data']['translations'][0]['translatedText']
                else:
                    translations[key] = 'x'

            self.header('Content-Type', 'text/plain; charset=utf-8')
            self.echo('# -*- coding: utf-8 -*-\n')
            self.echo('def translation():')
            self.echo('   return {')
            for key, value in translations.iteritems():
                self.echo('        \'' + key + '\': \'' + value + '\',')
            self.echo('}')
        else:
            self.echo('ERROR: No language "' + from_lang + '"')


class TranslateCSV(boRequestHandler):
    def get(self):
        #self.header('Content-Type', 'text/csv; charset=utf-8')
        for t in TagType().all():
            if t.name_russian:
                self.echo('"' + t.name + '", "' + t.name_estonian + '", "' + t.name_russian + '"')
            else:
                self.echo('"' + t.name + '", "' + t.name_estonian + '", ""')


def main():
    Route([
             ('/admin', ShowAdmin),
             ('/admin/library', AddLibrary),
             ('/admin/invite', SendInvites),
             (r'/admin/translate/(.*)/(.*)', TranslateAll),
             ('/admin/translate_csv', TranslateCSV),
            ])


if __name__ == '__main__':
    main()