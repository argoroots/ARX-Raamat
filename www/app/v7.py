from tornado.web import RequestHandler
from tornado.options import options
from tornado import database
from urllib import unquote


class myDb():
    @property
    def db(self):
        return database.Connection(
            host        = options.mysql_host,
            database    = options.mysql_database,
            user        = options.mysql_user,
            password    = options.mysql_password,
        )


class Show7Info(RequestHandler):
    def get(self):
        self.render('v7/info.html')


class ShowHelp(RequestHandler):
    def get(self, url = ''):
        self.render('v7/help.html')


class RegisterNew(RequestHandler):
    def get(self):

        if unquote(self.get_argument('voti', '')).lower() == 'true':
            programm_id = unquote(self.get_argument('id', ''))
            u = myDb().db.get('SELECT * FROM v7kasutajad WHERE programm_id = %s LIMIT 1;', programm_id)

            if not u:
                message = 'VIGA: Vale Programmi ID! Programm tuleb enne registreerida.'
            else:
                message = 'OK: '
                message = message + (str(u.asutus_id) + '##################################################')[:50]
                message = message + (str(u.asutus_nimi) + '##################################################')[:50]
                message = message + (str(u.asutus_aadress) + '##################################################')[:50]
                message = message + (str(u.asutus_linn) + '##################################################')[:50]
                message = message + (str(u.asutus_postiindeks) + '##################################################')[:50]
                message = message + (str(u.asutus_maakond) + '##################################################')[:50]
                message = message + (str(u.asutus_telefon) + '##################################################')[:50]
                message = message + ('Standard##########################################')

            return self.write(message)


        if unquote(self.get_argument('Programm_ID', '')):
            max_asutus = myDb().db.get('SELECT MAX(asutus_id) AS last_id FROM v7kasutajad;')
            if max_asutus['last_id'] < 100000:
                asutus_id = 100001
            else:
                asutus_id = max_asutus['last_id'] + 1

            myDb().db.execute('INSERT INTO v7kasutajad SET asutus_id = %s, asutus_nimi = %s, asutus_regnumber = %s, asutus_juhataja = %s, asutus_aadress = %s, asutus_linn = %s, asutus_postiindeks = %s, asutus_maakond = %s, asutus_telefon = %s, asutus_email = %s, kontaktisik_nimi = %s, kontaktisik_telefon = %s, kontaktisik_email = %s, programm_id = %s, programm_versioon = %s, ip = %s;',
                asutus_id,
                unquote(self.get_argument('Asutus_Nimi', 'NIMETU')),
                unquote(self.get_argument('Asutus_RegNumber', '')),
                unquote(self.get_argument('Asutus_Juhataja', '')),
                unquote(self.get_argument('Asutus_Aadress', '')),
                unquote(self.get_argument('Asutus_Linn', '')),
                unquote(self.get_argument('Asutus_Postiindeks', '')),
                unquote(self.get_argument('Asutus_Maakond', '')),
                unquote(self.get_argument('Asutus_Telefon', '')),
                unquote(self.get_argument('Asutus_Email', '')),
                unquote(self.get_argument('Kontaktisik_Nimi', '')),
                unquote(self.get_argument('Kontaktisik_Telefon', '')),
                unquote(self.get_argument('Kontaktisik_Email', '')),
                unquote(self.get_argument('Programm_ID', '')),
                unquote(self.get_argument('Programm_VersiooniNr', '')),
                self.request.remote_ip
            )
            self.write('ARX-Raamat REG_OK')


class CheckVersion(RequestHandler):
    def get(self):
        myDb().db.execute('INSERT INTO v7kasutajad SET asutus_id = %s, asutus_nimi = %s, programm_id = %s, programm_versioon = %s, ip = %s ON DUPLICATE KEY UPDATE kontroll_kokku = kontroll_kokku + 1, ip = %s;',
            unquote(self.get_argument('Asutus_ID', '0')),
            unquote(self.get_argument('Asutus_Nimi', '')),
            unquote(self.get_argument('Programm_ID', '')),
            unquote(self.get_argument('Programm_Versioon', '')),
            self.request.remote_ip,
            self.request.remote_ip
        )
        self.write('ARX-Raamat 7.0.150')


class ErrorReport(RequestHandler):
    def get(self):
        myDb().db.execute('INSERT INTO v7vead SET asutus_id = %s, asutus_nimi = %s, programm_id = %s, programm_versioon = %s, viga_funktsioon = %s, viga_number = %s, viga_tekst = %s, ip = %s;',
            unquote(self.get_argument('Asutus_ID', '0')),
            unquote(self.get_argument('Asutus_Nimi', '')),
            unquote(self.get_argument('Programm_ID', '')),
            unquote(self.get_argument('Programm_VersiooniNr', '')),
            unquote(self.get_argument('Viga_Funktsioon', '')),
            unquote(self.get_argument('Viga_Nr', '')),
            unquote(self.get_argument('Viga_Tekst', '')),
            self.request.remote_ip
        )
        myDb().db.execute('INSERT INTO v7kasutajad SET asutus_id = %s, asutus_nimi = %s, programm_id = %s, programm_versioon = %s, ip = %s ON DUPLICATE KEY UPDATE kontroll_kokku = kontroll_kokku + 1, ip = %s;',
            unquote(self.get_argument('Asutus_ID', '0')),
            unquote(self.get_argument('Asutus_Nimi', '')),
            unquote(self.get_argument('Programm_ID', '')),
            unquote(self.get_argument('Programm_VersiooniNr', '')),
            self.request.remote_ip,
            self.request.remote_ip
        )


handlers = [
    (r'/', Show7Info),
    (r'/help(.*)', ShowHelp),
    ('/registreerimine.php', RegisterNew),
    ('/versioon.php', CheckVersion),
    ('/vearaport.php', ErrorReport),
]
