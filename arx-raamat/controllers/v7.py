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


def main():
    Route([
             ('/', ShowInfo),
             ('/v7/setup', GetSetup),
             ('/v7/keygen', GetKegen),
             ('/v7/manual', GetManual),
            ])


if __name__ == '__main__':
    main()