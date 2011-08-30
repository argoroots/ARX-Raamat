from google.appengine.api import memcache
from google.appengine.api import urlfetch
from urllib import quote
from django.utils import simplejson
from hashlib import md5
import re

from BeautifulSoup import BeautifulSoup


#http://www.loc.gov/marc/bibliographic/
MARCMAP = {
    '020a': 'isbn',
    '022a': 'issn',
    '041a': 'language',
    '041h': 'original_language',
    '072a': 'udc',
    '080a': 'udc',
    '245a': 'title',
    '245b': 'subtitle',
    '245p': 'subtitle',
    '245n': 'number',
    '250a': 'edition',
    '260a': 'publishing_place',
    '260b': 'publisher',
    '260c': 'publishing_date',
    '300a': 'pages',
    '300c': 'dimensions',
    '440a': 'series',
    '440p': 'series',
    '440n': 'series_number',
    '440v': 'series_number',
    '500a': 'notes',
    '501a': 'notes',
    '502a': 'notes',
    '504a': 'notes',
    '505a': 'notes',
    '520a': 'notes',
    '525a': 'notes',
    '530a': 'notes',
    '650a': 'tag',
    '655a': 'tag',
}


def EsterSearch(search_term, records):
    try:
        z39_url = 'http://z39.arx.ee/?r=' + str(records) + '&q=' + quote(search_term.encode('utf-8'))
        json_str = urlfetch.fetch(z39_url, deadline=10).content

        data = []
        for record in simplejson.loads(json_str):
            if GetType(record) == 'book':
                item = GetRecord(record)
                item['marc21'] = simplejson.dumps(record)
                item['authors'] = GetAuthors(record)
                item['id'] = GetID(record)

                data.append(item)

                if memcache.get('ester_item_' + item['id']):
                    memcache.replace(
                        key = 'ester_item_' + item['id'],
                        value = (item),
                        time = 86400
                    )
                else:
                    memcache.add(
                        key = 'ester_item_' + item['id'],
                        value = (item),
                        time = 86400
                    )

        return data
    except:
        pass


def EsterGetByID(id):
    return memcache.get('ester_item_' + id)


def GetRecord(record):
    data = {}
    for key, field in record.iteritems():
        for value in field:
            for tagkey, tagvalue in value.iteritems():
                if key + tagkey in MARCMAP:
                    tagvalue = CleanData(key + tagkey, tagvalue)
                    if MARCMAP[key + tagkey] not in data:
                        data[MARCMAP[key + tagkey]] = []
                    data[MARCMAP[key + tagkey]].append(tagvalue)
    return data


def CleanData(tag, value):
    if value[0:1] == '[' and value[-1] == ']':
        value = value[1:][:-1]
    if tag == '260c' and not value[0:1].isdigit():
        value = value[1:]

    return value


def GetAuthors(record):
    result = []
    if '100' in record:
        for row in record['100']:
            d = {}
            if 'a' in row:
                d['name'] = row['a']

            if 'd' in row:
                d['date'] = row['d']
            else:
                d['date'] = None

            d['role'] = 'author'

            result.append(d)

    if '700' in record:
        for row in record['700']:
            d = {}
            if 'a' in row:
                d['name'] = row['a']

            if 'd' in row:
                d['date'] = row['d']
            else:
                d['date'] = None

            if 'e' in row:
                d['role'] = row['e']
            else:
                d['role'] = 'author'

            result.append(d)

    return result


def GetType(record):

    if '000' in record:
        a = record['000'][0]['a'][6:7]
        b = record['000'][0]['a'][7:8]

        if a == 'a':
            if 'acdm'.find(b) > 0:
                return 'book'
            if 'bis'.find(b) > 0:
                return 'series'

        if a == 't':
            return 'book'

        if a == 'p':
            return 'mixed'

        if a == 'm':
            return 'file'

        if 'ef'.find(a) > 0:
            return 'map'

        if 'gkor'.find(a) > 0:
            return 'visual'

        if 'sdij'.find(a) > 0:
            return 'music'


def GetID(record):

    key = ''
    if '020' in record:
        if 'a' in record['020'][0]:
            key = key + record['020'][0]['a']

    if '100' in record:
        if 'a' in record['100'][0]:
            key = key + CleanData('100a', record['100'][0]['a'])

    if '245' in record:
        if 'a' in record['245'][0]:
            key = key + CleanData('245a', record['245'][0]['a'])
        if 'n' in record['245'][0]:
            key = key + CleanData('245n', record['245'][0]['n'])

    if '260' in record:
        if 'c' in record['260'][0]:
            key = key + CleanData('260c', record['260'][0]['c'])
        if 'a' in record['260'][0]:
            key = key + CleanData('260a', record['260'][0]['a'])

    key = re.sub(r'[\s\-\?\!\#\&\.\,\:\;\"\'\[\]\(\)]', '', key).upper().encode('utf-8')
    key = 'ester-' + md5(key).hexdigest()

    return key