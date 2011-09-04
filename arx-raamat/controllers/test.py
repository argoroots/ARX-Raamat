# -*- coding: windows-1251 -*-

from google.appengine.api import memcache
from urllib import unquote
import urllib

import chardet

from bo import *
from database.item import *
from importers.ester import *
from importers.apollo import *
from importers.rahvaraamat import *
from importers.raamatukoi import *
from importers.googlebooks import *
from importers.amazon import *


class MarcTest(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain; charset=UTF-8'

        marcmap = {
            '020':  'isbn',
            '022':  'issn',
            '041':  'language',
            '041h': 'original_language',
            '072':  'udc',
            '080':  'udc',
            '245':  'title',
            '245b': 'subtitle',
            '245p': 'subtitle',
            '245n': 'number',
            '250':  'edition',
            '260':  'publishing_place',
            '260b': 'publisher',
            '260c': 'publishing_date',
            '300':  'pages',
            '300c': 'dimensions',
            '440':  'series',
            '440p': 'series',
            '440n': 'series_number',
            '440v': 'series_number',
            '500':  'notes',
            '501':  'notes',
            '502':  'notes',
            '504':  'notes',
            '505':  'notes',
            '520':  'notes',
            '525':  'notes',
            '530':  'notes',
            '650':  'tag',
            '655':  'tag',
        }

        data = """
LEADER 00000nam  2200000 i 4500
008    080305s2007    sp     | |||||||| f|est
020    9788498199215 (41. raamat)
020    9788498198294 (sari)
040    ErRR|best|cErRR|dErTlnKR|dErTTUR
041 1  est|heng
044    er|asp
072  7 821-93|2udkrb
080    821.111-93-312.9|2est
100 1  Tolkien, J. R. R.,|d1892-1973
245 10 Kääbik, ehk, Sinna ja tagasi /|cJ. R. R. Tolkien ; inglise
       keelest tõlkinud Lia Rajandi ; [värsside tõlge: Harald
       Rajamets]
246 19 The hobbit, or, There and back again.|gEesti keeles
260    Madrid :|bMediasat Group ;|a[Tallinn] :|bEesti Päevaleht
       [levitaja],|cc2007
300    216, [3] lk. ;|c22 cm
440  0 Eesti Päevalehe romaaniklassika ;|v41
534    |pTõlke esitrükk:|cTallinn : Eesti Raamat, 1977
650  9 inglise
655  9 noorsookirjandus
655  9 fantaasiaromaanid
700 1  Rajandi, Lia,|d1929-,|etõlkija
700 1  Rajamets, Harald,|d1924-2007,|etõlkija
740 0  Romaaniklassika.|n41
910 0  RMT 2008:03|b978-84-9819-921-5 (41. raamat)|b978-84-9819-
       829-4 (sari)
910 0  EST
933    20080218
950    |tRBK lembi|sNAO merle 2008-03
952    |sTO Maire-03.08
953    |pklak(+080,+650,+655)
970    20110209_tenno
977    |kKTO reet 2008-01
"""

        marc = {}
        rows = []
        rownum = 0
        for row in data.strip().split('\n'):
            if row[:7].strip():
                rownum += 1
                rows.append(row)
            else:
                rows[rownum-1] += row[7:]

        for row in rows:
            key = row[:3]
            values = row[7:].split('|')
            if values[0]:
                if key in marcmap:
                    marckey = marcmap[key]
                    if marckey not in marc:
                        marc[marckey] = []
                    marc[marckey].append(values[0].strip(' /;:'))
            for v in values[1:]:
                if v:
                    if key+v[0] in marcmap:
                        marckey = marcmap[key+v[0]]
                        if marckey not in marc:
                            marc[marckey] = []
                        marc[marckey].append(v[1:].strip(' /;:'))


        self.response.out.write(data+'\n\n\n')
        for tagkey, tagvalue in marc.iteritems():
            self.response.out.write(tagkey+' '+str(tagvalue)+'\n')


class AmazonSearchTest(webapp.RequestHandler):
    def get(self, url):
        keywords = unquote(url).decode('utf8').strip('/')

        result = SearchBook(keywords)
        strng = ''
        for item in result:
            for i in item:
            	strng = strng + i + ' => ' + item[i] + '<br />'
            strng = strng + '<hr />'
        self.response.out.write(strng)

# N.B! Some values can be None or a list; then the test function will fail
class AmazonTest(webapp.RequestHandler):
    def get(self, url):
        keywords = unquote(url).decode('utf8').strip('/')

        result = GetBook(keywords)
        strng = ''
        for item in result:

            strng = strng + item + ' => ' + result[item] + '<br />'

        self.response.out.write(strng)

class Search(webapp.RequestHandler):
    def get(self, string):

        result = EsterSearch(string, 30)

        #self.response.out.write(result)

        self.response.out.write('<pre>')
        if result:
            for row in result:
                for tag, value in row.iteritems():
                    if tag != 'id1':
                        self.response.out.write(tag + ' = ' + str(value) + '\n')

                self.response.out.write('\n')
        self.response.out.write('</pre>')


class Scan(webapp.RequestHandler):
    def get(self, code):

        book = None
        picture = None

        if code:
            result = EsterSearch(code, 1)
            if result:
                book = result[0]
            picture = ShowImage(code)

        View(self, '', 'scan.html', {
            'book': book,
            'picture': picture,
            'code': code
        })


def ShowImage(isbn):
    result = None
    result = RahvaraamatImageByISBN(isbn)
    if not result:
        result = RaamatukoiImageByISBN(isbn)
        if not result:
            result = GoogleImageByISBN(isbn)
    return result

class TagTypeUpdate(webapp.RequestHandler):
    def get(self):
        for tt in TagType().all():
            tt.is_visible = True
            tt.put()


def main():
    Route([
             (r'/test/search/(.*)', Search),
             (r'/test/scan/(.*)', Scan),
             ('/test/amazon/search/(.*)', AmazonSearchTest),
             ('/test/amazon/(.*)', AmazonTest),
             ('/test/ttu', TagTypeUpdate),
             ('/test/marc', MarcTest),
            ])


if __name__ == '__main__':
    main()