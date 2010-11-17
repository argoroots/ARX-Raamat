import urllib
import hashlib
from time import time
from google.appengine.api import urlfetch
from django.utils import simplejson

from bo import *
from database import *


class ShowAdmin(webapp.RequestHandler):
    def get(self):
        l = db.Query(Library).order('name').fetch(1000)
        View(self, '', 'admin.html', {
            'libraries': l
        })


class AddLibrary(webapp.RequestHandler):
    def post(self):
        name = self.request.get('library').strip('')
        l = db.Query(Library).filter('name', name).get()
        if not l:
            l = Library()
            l.name = name
            l.put()
        self.redirect('/admin')


class SendInvites(webapp.RequestHandler):
    def post(self):
        emails = self.request.get('emails')
        if emails:
            for email in StrToList(emails):
                key = hashlib.md5(str(time()) + email).hexdigest()

                p = db.Query(Person).filter('email =', email).get()
                if not p:
                    p = Person()
                    p.library = db.Key(self.request.get('library'))
                    p.email = email.lower()
                    p.type = 'admin'
                    p.status = 'new'

                p.activation_key = key
                p.save()

                link = 'http://' + SYSTEM_URL + '/signup/' + str(p.key().id()) + '/' + key

                SendMail(
                    to = email,
                    subject = Translate('invitation_subject'),
                    message = Translate('invitation_email') % link
                )
        self.redirect('/admin')


class TranslateAll(webapp.RequestHandler):
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

            self.response.out.write('# -*- coding: utf-8 -*-\n\n')
            self.response.out.write('def translation():\n')
            self.response.out.write('   return {\n')
            for key, value in translations.iteritems():
                self.response.out.write('        \'' + key + '\': \'' + value + '\',\n')
            self.response.out.write('}')
        else:
            self.response.out.write('ERROR: No language "' + from_lang + '"')


def main():
    Route([
             ('/admin', ShowAdmin),
             ('/admin/library', AddLibrary),
             ('/admin/invite', SendInvites),
             ('/admin/translate/(.*)/(.*)', TranslateAll),
            ])


if __name__ == '__main__':
    main()