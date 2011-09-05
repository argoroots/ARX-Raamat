from google.appengine.api import memcache
from google.appengine.api import urlfetch

from BeautifulSoup import BeautifulSoup


def EsterSearch(search_term):
    items = []
    if len(search_term) == 13 and search_term.isdigit():
        soup = BeautifulSoup(urlfetch.fetch('http://tallinn.ester.ee/search*est/i?SEARCH='+search_term+'&searchscope=1&SUBMIT=OTSI').content)
        id = soup.find('a', attrs={'id': 'recordnum'})['href'].replace('http://tallinn.ester.ee/record=', '').replace('~S1', '').replace('*est', '').strip()
        items.append(EsterGetByID(id))
    else:
        soup = BeautifulSoup(urlfetch.fetch('http://tallinn.ester.ee/search*est/X?SEARCH='+search_term+'&searchscope=1&SUBMIT=OTSI').content)
        for i in soup.findAll('table', attrs={'class': 'browseList'}):
            cells = i.findAll('td')
            id = cells[0].input['value'].strip()
            title = cells[1].span.a.contents[0].strip()
            isbn = cells[1].find(text='ISBN/ISSN').next.strip(':&nbsp;\n ').strip()
            year = cells[4].contents[0].strip()
            items.append({
                'id': id,
                'isbn': [isbn],
                'title': [title],
                'publishing_date': [year],
            })

    return items


def EsterGetByID(id):
    ester_url = 'http://tallinn.ester.ee/search~S1?/.'+id+'/.'+id+'/1%2C1%2C1%2CB/marc~'+id
    soup = BeautifulSoup(urlfetch.fetch(ester_url).content)
    item = ParseMARC(soup.find('pre').contents[0])
    item['id'] = id
    return item


def ParseMARC(data):
    #http://www.loc.gov/marc/bibliographic/
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
    return marc


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