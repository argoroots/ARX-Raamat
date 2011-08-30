from django.utils import simplejson
import urllib
import base64

from bo import *
from database import *
import chardet


class Upload(webapp.RequestHandler):
    def post(self):
        if self.request.get('json'):
            json_str = self.request.get('json')
            scarset = chardet.detect(json_str)

            #json_str = base64.b64decode(json_str)

            json_str = json_str.decode(scarset['encoding'])

            d = v7data()
            d.item_json = json_str
            d.put()

            #item = simplejson.loads(json_str.decode(scarset['encoding']))

            self.response.out.write(scarset)


def main():
    Route([
             ('/bulka', Upload),
            ])


if __name__ == '__main__':
    main()