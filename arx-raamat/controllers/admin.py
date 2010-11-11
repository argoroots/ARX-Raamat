import hashlib
from time import time

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


def main():
    Route([
             ('/admin', ShowAdmin),
             ('/admin/library', AddLibrary),
             ('/admin/invite', SendInvites),
            ])


if __name__ == '__main__':
    main()