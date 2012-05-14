from os import path

import tornado.ioloop
import tornado.locale
import tornado.web
import tornado.httpserver
import tornado.database
import tornado.options
from tornado.options import define, options


define('debug',          help = 'run on debug mode',        type = str, default='False')
define('port',           help = 'run on the given port',    type = int)
define('mysql_host',     help = 'mysql database host',      type = str)
define('mysql_database', help = 'mysql database name',      type = str)
define('mysql_user',     help = 'mysql database user',      type = str)
define('mysql_password', help = 'mysql database password',  type = str)


controllers = [
    'v7',
]


class myApplication(tornado.web.Application):
    def __init__(self):
        handlers = []
        for controller in controllers:
            c = __import__ (controller, globals(), locals(), ['*'], -1)
            handlers.extend(c.handlers)

        settings = {
            'template_path':    path.join(path.dirname(__file__), '..', 'templates'),
            'static_path':      path.join(path.dirname(__file__), '..', 'static'),
            'debug':            True if str(options.debug).lower() == 'true' else False,
        }

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_config_file(path.join(path.dirname(__file__), '..', 'app.config'))
    tornado.options.parse_command_line()
    tornado.httpserver.HTTPServer(myApplication(), xheaders=True).listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
