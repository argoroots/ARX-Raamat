# -*- coding: utf-8 -*-

from datetime import datetime
from urllib import unquote
from cgi import escape

from bo import *
from database import *


class ShowInfo(webapp.RequestHandler):
    def get(self):
        page_meta = """
            <!-- Orbit -->
            <script type="text/javascript" src="/javascript/jquery.orbit.min.js"></script>
            <link href="/css/orbit.css" rel="stylesheet" type="text/css" />
        """

        View(self, '7', 'v7.html', {'page_meta':page_meta})


class GetSetup(webapp.RequestHandler):
    def get(self):
        d = v7download()
        d.type = 'setup'
        d.ip = self.request.remote_addr
        d.put()
        self.redirect('/v7setup/ARX-Raamat7_Setup.exe')


class GetKegen(webapp.RequestHandler):
    def get(self):
        d = v7download()
        d.type = 'keygen'
        d.ip = self.request.remote_addr
        d.put()
        self.redirect('/v7setup/ARX-Raamat7_Voti.exe')


class GetManual(webapp.RequestHandler):
    def get(self):
        d = v7download()
        d.type = 'manual'
        d.ip = self.request.remote_addr
        d.put()
        self.redirect('/v7setup/ARX-Raamat7_Kasutusjuhend.pdf')


class RegisterNew(webapp.RequestHandler):
    def get(self):

        if unquote(self.request.get('voti')) == 'true':

            programm_id = unquote(self.request.get('id'))
            u = db.Query(v7user).filter('programm_id', programm_id).order('-library_id').get()

            if not u:
                message = 'VIGA: Programmi ID ei ole õige! Registreerige programm enne võtmefaili genereerimist.'
            else:
                message = 'OK: '
                message = message + (str(u.library_id) + '##################################################')[:50]
                message = message + (u.library_name + '##################################################')[:50]
                message = message + (u.library_address + '##################################################')[:50]
                message = message + (u.library_city + '##################################################')[:50]
                message = message + (u.library_zip + '##################################################')[:50]
                message = message + (u.library_county + '##################################################')[:50]
                message = message + (u.library_phone + '##################################################')[:50]
                message = message + ('Standard##########################################')

            SendMail(
                to = 'argo@roots.ee',
                subject = 'Key - ' + u.library_name,
                message = u.library_name
            )

            self.response.out.write(message)

        else:
            if unquote(self.request.get('Programm_ID')):
                if unquote(self.request.get('Asutus_Nimi')):
                    library_name = unquote(self.request.get('Asutus_Nimi'))
                else:
                    library_name = 'NIMETU'
                library_address = unquote(self.request.get('Asutus_Aadress'))
                library_city = unquote(self.request.get('Asutus_Linn'))
                library_zip = unquote(self.request.get('Asutus_Postiindeks'))
                library_county = unquote(self.request.get('Asutus_Maakond'))
                library_phone = unquote(self.request.get('Asutus_Telefon'))
                library_mail = unquote(self.request.get('Asutus_Email'))
                contact_name = unquote(self.request.get('Kontaktisik_Nimi'))
                contact_phone = unquote(self.request.get('Kontaktisik_Telefon'))
                contact_mail = unquote(self.request.get('Kontaktisik_Email'))
                programm_id = unquote(self.request.get('Programm_ID'))

                umax = db.Query(v7user).filter('library_id >', 10000).order('-library_id').get()
                if umax:
                    library_id = umax.library_id + 1
                else:
                    library_id = 10001

                u = v7user()
                u.library_id = library_id
                u.library_name = library_name
                u.library_address = library_address
                u.library_city = library_city
                u.library_zip = library_zip
                u.library_county = library_county
                u.library_phone = library_phone
                u.library_mail = library_mail
                u.contact_name = contact_name
                u.contact_phone = contact_phone
                u.contact_mail = contact_mail
                u.programm_id = programm_id

                u.put()

                SendMail(
                    to = 'argo@roots.ee',
                    subject = 'Reg - ' + u.library_name,
                    message = u.library_name
                )

            self.response.out.write('ARX-Raamat REG_OK')


class CheckVersion(webapp.RequestHandler):
    def get(self):

        if unquote(self.request.get('Asutus_ID')):
            library_id = int(unquote(self.request.get('Asutus_ID', 0)))
            library_name = unquote(self.request.get('Asutus_Nimi'))
            programm_id = unquote(self.request.get('Programm_ID'))

            u = db.Query(v7user).filter('library_id', library_id).filter('programm_id', programm_id).get()

            if not u:
                u = v7user()
                u.library_id = library_id
                u.library_name = library_name
                u.programm_id = programm_id
                u.check_count = 1
            else:
                u.check_count = u.check_count + 1

            u.check_lasttime = datetime.now()
            u.put()

        self.response.out.write('ARX-Raamat 7.0.150')


class ErrorReport(webapp.RequestHandler):
    def get(self):
        library_id = int(unquote(self.request.get('Asutus_ID', 0)))
        library_name = unquote(self.request.get('Asutus_Nimi'))
        programm_id = unquote(self.request.get('Programm_ID'))
        error_function = unquote(self.request.get('Viga_Funktsioon'))
        error_number = unquote(self.request.get('Viga_Nr'))
        error_text = unquote(self.request.get('Viga_Tekst'))

        u = v7error()
        u.library_id = library_id
        u.library_name = library_name
        u.programm_id = programm_id
        u.error_function = error_function
        u.error_number = error_number
        u.error_text = error_text
        u.put()

        SendMail(
            to = 'argo@roots.ee',
            subject = 'Err - ' + u.error_number + ': ' + u.error_function,
            message = 'ERROR:<br><br>' + u.error_text
        )


class GetHelp(webapp.RequestHandler):
    def get(self, url = None):
        View(self, '', 'v7help.html')


def main():
    Route([
             ('/v7', ShowInfo),
             ('/v7/setup', GetSetup),
             ('/v7/keygen', GetKegen),
             ('/v7/manual', GetManual),
             (r'/help(.*)', GetHelp),
             ('/registreerimine.php', RegisterNew),
             ('/versioon.php', CheckVersion),
             ('/vearaport.php', ErrorReport),
            ])


if __name__ == '__main__':
    main()