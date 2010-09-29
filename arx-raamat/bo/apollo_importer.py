import os
import re
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

# Lookup book data from Apollo.ee DB by book ID
# Input: Book ID
# Output: Dict with Apollo's info
def GetBookByID(book_id):
    apollo_url = 'http://apollo.ee/product.php/' + book_id
    soup = BeautifulSoup(GetSource(apollo_url))
    data_object = soup.find('div', attrs={'class' : 'wrapRaamat'})
    
    # Start searching relevant info from data_object and prepare it for returning in dict 'data'

    # Authors need special parsing - one book can have multiple authors.
    authors = []
    for n in data_object.findAll('a', attrs={'title': 'Veel sellelt autorilt'}):
        authors.append(''.join(n.findAll(text=True)))

    # Date published
    date_position = str(data_object).find('Ilmumisaasta')+12
    date_published = str(data_object)[(date_position+1):(date_position+5)]
    
    # This is the main data dict
    data = {'ID': book_id,
            'title': ''.join(data_object.h2),
            'description': ''.join(StripHTML(data_object.p)),
            'authors': authors,
            'date_published': date_published}
    return data

# Return the HTML of input URL
def GetSource(target_url):
    headers = { 'User-Agent' : 'Mozilla/5 (Solaris 10) Gecko' }
    values = {} # Not needed
    data = urllib.urlencode(values) # Not needed
    request = urllib2.Request(target_url, data, headers)
    response = urllib2.urlopen(request)
    source = response.read()
    return source

# Strip out any HTML tags found in input string
def StripHTML(data):
    data = str(data)
    p = re.compile(r'<.*?>')
    return p.sub('', data)