import os
import logging
import chardet
import tornado.ioloop
import tornado.web
import tornado.httpserver

from urllib import unquote
from raven.contrib.tornado import AsyncSentryClient


# global variables (and list of all used environment variables)
APP_VERSION = os.getenv('VERSION', tornado.version)
APP_DEBUG   = os.getenv('DEBUG', 'false')
APP_PORT    = os.getenv('PORT', 3000)
APP_SENTRY  = os.getenv('SENTRY_DSN')


class ShowHelp(tornado.web.RequestHandler):
    def get(self, url = ''):
        self.render('help.html')


class Show7info(tornado.web.RequestHandler):
    def get(self, url = ''):
        self.render('info.html')


class ShowLetter(tornado.web.RequestHandler):
    def get(self, page=None):
        self.render('letter.html')


class RegisterNew(tornado.web.RequestHandler):
    def get(self, url = ''):

        if unquote(self.get_argument('voti', '')).lower() == 'true':
            programm_id = unquote(self.get_argument('id', ''))
            # u = myDb().db.get('SELECT * FROM v7kasutajad WHERE programm_id = %s ORDER BY id DESC LIMIT 1;', programm_id)

            # if not u:
            #     message = 'VIGA: Vale Programmi ID! Programm tuleb enne registreerida.'
            # else:
            #     message = 'OK: '
            #     message = message + ('%s##################################################' % u.asutus_id)[:50]
            #     message = message + ('%s##################################################' % u.asutus_nimi)[:50]
            #     message = message + ('%s##################################################' % u.asutus_aadress)[:50]
            #     message = message + ('%s##################################################' % u.asutus_linn)[:50]
            #     message = message + ('%s##################################################' % u.asutus_postiindeks)[:50]
            #     message = message + ('%s##################################################' % u.asutus_maakond)[:50]
            #     message = message + ('%s##################################################' % u.asutus_telefon)[:50]
            #     message = message + ('Standard##########################################')
            u = {
                'asutus_id': 10001,
                'asutus_nimi': 'Argo Roots',
            }
            message = 'OK: '
            message = message + ('%s##################################################' % u.get('asutus_id'))[:50]
            message = message + ('%s##################################################' % u.get('asutus_nimi'))[:50]
            message = message + ('%s##################################################' % u.get('asutus_aadress'))[:50]
            message = message + ('%s##################################################' % u.get('asutus_linn'))[:50]
            message = message + ('%s##################################################' % u.get('asutus_postiindeks'))[:50]
            message = message + ('%s##################################################' % u.get('asutus_maakond'))[:50]
            message = message + ('%s##################################################' % u.get('asutus_telefon'))[:50]
            message = message + ('Standard##########################################')

            return self.write(message)

        if unquote(self.get_argument('Programm_ID', '')):
            # max_asutus = myDb().db.get('SELECT MAX(asutus_id) AS last_id FROM v7kasutajad;')
            # if max_asutus['last_id'] < 100000:
            #     asutus_id = 100001
            # else:
            #     asutus_id = max_asutus['last_id'] + 1

            # myDb().db.execute('INSERT INTO v7kasutajad SET asutus_id = %s, asutus_nimi = %s, asutus_regnumber = %s, asutus_juhataja = %s, asutus_aadress = %s, asutus_linn = %s, asutus_postiindeks = %s, asutus_maakond = %s, asutus_telefon = %s, asutus_email = %s, kontaktisik_nimi = %s, kontaktisik_telefon = %s, kontaktisik_email = %s, programm_id = %s, programm_versioon = %s, ip = %s;',
            #     asutus_id,
            #     unquote(self.get_argument('Asutus_Nimi', '')),
            #     unquote(self.get_argument('Asutus_RegNumber', '')),
            #     unquote(self.get_argument('Asutus_Juhataja', '')),
            #     unquote(self.get_argument('Asutus_Aadress', '')),
            #     unquote(self.get_argument('Asutus_Linn', '')),
            #     unquote(self.get_argument('Asutus_Postiindeks', '')),
            #     unquote(self.get_argument('Asutus_Maakond', '')),
            #     unquote(self.get_argument('Asutus_Telefon', '')),
            #     unquote(self.get_argument('Asutus_Email', '')),
            #     unquote(self.get_argument('Kontaktisik_Nimi', '')),
            #     unquote(self.get_argument('Kontaktisik_Telefon', '')),
            #     unquote(self.get_argument('Kontaktisik_Email', '')),
            #     unquote(self.get_argument('Programm_ID', '')),
            #     unquote(self.get_argument('Programm_VersiooniNr', '')),
            #     self.request.remote_ip
            # )
            self.write('ARX-Raamat REG_OK')


class CheckVersion(tornado.web.RequestHandler):
    def get(self, url = ''):
        # myDb().db.execute('INSERT INTO v7kasutajad SET asutus_id = %s, asutus_nimi = %s, programm_id = %s, programm_versioon = %s, ip = %s ON DUPLICATE KEY UPDATE kontroll_kokku = kontroll_kokku + 1, ip = %s;',
        #     unquote(self.get_argument('Asutus_ID', '0')),
        #     unquote(self.get_argument('Asutus_Nimi', '')),
        #     unquote(self.get_argument('Programm_ID', '')),
        #     unquote(self.get_argument('Programm_Versioon', '')),
        #     self.request.remote_ip,
        #     self.request.remote_ip
        # )
        self.write('ARX-Raamat 7.0.150')


class ErrorReport(tornado.web.RequestHandler):
    def get(self, url = ''):
        pass
        # myDb().db.execute('INSERT INTO v7vead SET asutus_id = %s, asutus_nimi = %s, programm_id = %s, programm_versioon = %s, viga_funktsioon = %s, viga_number = %s, viga_tekst = %s, ip = %s;',
        #     unquote(self.get_argument('Asutus_ID', '0')),
        #     unquote(self.get_argument('Asutus_Nimi', '')),
        #     unquote(self.get_argument('Programm_ID', '')),
        #     unquote(self.get_argument('Programm_VersiooniNr', '')),
        #     unquote(self.get_argument('Viga_Funktsioon', '')),
        #     unquote(self.get_argument('Viga_Nr', '')),
        #     unquote(self.get_argument('Viga_Tekst', '')),
        #     self.request.remote_ip
        # )
        # myDb().db.execute('INSERT INTO v7kasutajad SET asutus_id = %s, asutus_nimi = %s, programm_id = %s, programm_versioon = %s, ip = %s ON DUPLICATE KEY UPDATE kontroll_kokku = kontroll_kokku + 1, ip = %s;',
        #     unquote(self.get_argument('Asutus_ID', '0')),
        #     unquote(self.get_argument('Asutus_Nimi', '')),
        #     unquote(self.get_argument('Programm_ID', '')),
        #     unquote(self.get_argument('Programm_VersiooniNr', '')),
        #     self.request.remote_ip,
        #     self.request.remote_ip
        # )


class CharDetection(tornado.web.RequestHandler):
    def post(self):
        string = self.request.body
        if chardet.detect(string).get('encoding', None) in ['ISO-8859-2', 'ascii', 'windows-1252', 'windows-1255']:
            encoding = 'ISO-8859-2'
            self.write('EST - %s' % unicode(string, encoding).strip())
        else:
            encoding = 'windows-1251'
            self.write('RUS - %s' % unicode(string, encoding).strip())


class myApplication(tornado.web.Application):
    def __init__(self):
        handlers = [
            ('/chardet', CharDetection),
            (r'/help(.*)', ShowHelp),
            (r'/7(.*)', Show7info),
            (r'/registreerimine(.*)', RegisterNew),
            (r'/versioon(.*)', CheckVersion),
            (r'/vearaport(.*)', ErrorReport),
            (r'(.*)', ShowLetter),
        ]
        settings = {
            'template_path':    os.path.join(os.path.dirname(__file__), '..', 'templates'),
            'static_path':      os.path.join(os.path.dirname(__file__), '..', 'static'),
            'debug':            True if str(APP_DEBUG).lower() == 'true' else False,
            'xsrf_coocies':     True,
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    application = myApplication()
    application.sentry_client = AsyncSentryClient(dsn=APP_SENTRY, release=APP_VERSION)

    tornado.httpserver.HTTPServer(application, xheaders=True).listen(APP_PORT)
    tornado.ioloop.IOLoop.instance().start()
