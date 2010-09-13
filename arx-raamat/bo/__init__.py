import os
from google.appengine.api import mail
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

from bo.user import *
from bo.settings import *


def Route(url_mapping):
    application = webapp.WSGIApplication(url_mapping, debug=True)
    util.run_wsgi_app(application)


def View(self, page_title, templatefile, values={}):
    values['str'] = Translate()
    if page_title:
        values['site_name'] = SYSTEM_TITLE + ' - ' + Translate(page_title)
        values['page_title'] = Translate(page_title)
    else:
        values['site_name'] = SYSTEM_TITLE
        values['page_title'] = '&nbsp;'
    values['site_url'] = self.request.headers.get('host')
    values['user'] = User().current()
    values['logouturl'] = users.create_logout_url('/')
    path = os.path.join(os.path.dirname(__file__), '..', 'templates', templatefile)
    self.response.out.write(template.render(path, values))


def Translate(key = None):

    languagefile = 'translations.' + User().current().language

    l = __import__(languagefile, globals(), locals(), ['translation'], -1)

    if key:
        if key in l.translation():
            return l.translation()[key].decode('utf8')
        else:
            return key
    else:
        return l.translation()


def SendMail(to, subject, message):
    m = mail.EmailMessage()
    m.sender = SYSTEM_EMAIL
    m.to = to
    m.subject = subject
    m.html = message
    m.send()


def StrToList(string):
    return [x.strip() for x in string.strip().replace('\n', ' ').replace(',', ' ').replace(';', ' ').split(' ') if len(x.strip()) > 0]


def Rescale(img_data, width, height, halign='middle', valign='middle'):
    image = images.Image(img_data)

    desired_wh_ratio = float(width) / float(height)
    wh_ratio = float(image.width) / float(image.height)

    if desired_wh_ratio > wh_ratio:
        image.resize(width=width)
        image.execute_transforms()
        trim_y = (float(image.height - height) / 2) / image.height
        if valign == 'top':
            image.crop(0.0, 0.0, 1.0, 1 - (2 * trim_y))
        elif valign == 'bottom':
            image.crop(0.0, (2 * trim_y), 1.0, 1.0)
        else:
            image.crop(0.0, trim_y, 1.0, 1 - trim_y)
    else:
        image.resize(height=height)
        image.execute_transforms()
        trim_x = (float(image.width - width) / 2) / image.width
        if halign == 'left':
            image.crop(0.0, 0.0, 1 - (2 * trim_x), 1.0)
        elif halign == 'right':
            image.crop((2 * trim_x), 0.0, 1.0, 1.0)
        else:
            image.crop(trim_x, 0.0, 1 - trim_x, 1.0)

    return image.execute_transforms()