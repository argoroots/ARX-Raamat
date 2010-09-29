# -*- coding: utf-8 -*-
# Methods to get book information from apollo.ee
# Dev/maintainer: Ando Roots 2010

import re
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
import urllib


# Lookup book data from Apollo.ee DB by book ID
# Input: Book ID
# Output: Dict with Apollo's info
def GetBookByID(book_id):
    apollo_url = 'http://apollo.ee/product.php/' + book_id
    soup = BeautifulSoup(urlfetch.fetch(apollo_url).content)
    data_object = soup.find('div', attrs={'class' : 'wrapRaamat'})
    article_object = soup.find('div', attrs={'class' : 'wrapArtikkel'})
    
    # Authors need special parsing - one book can have multiple authors.
    authors = []
    for n in data_object.findAll('a', attrs={'title': 'Veel sellelt autorilt'}):
        authors.append(''.join(n.findAll(text=True)))    
    
    # This is the main data dict
    data = {'ID': book_id,
            'title': data_object.h2,
            'description': data_object.p,
            'authors': authors,
            'date_published': FindByPosition(data_object, 'Ilmumisaasta ', 4),
            'isbn': FindByPosition(data_object, 'ISBN-13 ',13),
            'publisher': ReSearch(data_object, r'Kirjastus (.*?)<br />'),
            'price_client': ''.join(soup.find('span', attrs={'class' : 'tooteSoodusHind'})),
            'price_normal': ''.join(soup.find('span', attrs={'class' : 'tooteHind'})),
            'format': ReSearch(data_object, r'Formaat (.*?);'),
            'number_of_pages': ReSearch(data_object, r'Lehekülgi (.*?);'),
            'img_url': 'http://apollo.ee' + article_object('img')[0]['src']}
    
    # Trouble with encoding, convert every member of data dict
    nice_data = {}
    for i in data:
        nice_data[i] = ConvertSoup(StripHTML(data[i]))
        
    return nice_data



# Search Apollo for a book. search_terms is a dict with form data.
# search_terms example: search_terms = {'name': 'muinasjutud', 'desc': 'lastele'}
# --- INCOMPLETE! ----
def SearchBook(search_terms):
    search_terms['search'] = 'Otsi'
    search_terms['department'] = '1'
    
    search_terms = urllib.urlencode(search_terms)
    apollo_url = 'http://apollo.ee/advsearch.php?'+search_terms
    soup = BeautifulSoup(urlfetch.fetch(apollo_url).content)
    data_object = soup.find('div', attrs={'class' : 'sisuWrap'})
    
    return str(data_object)




# Custom search. Get data that follows search_string in the haystack
# Example: haystack = 'Aasta 1967 talv' | needle = 'sta ' | length = 4
# 	...would return 1967
def FindByPosition(haystack, needle, length):
	position = str(haystack).find(str(needle))+len(needle)
	return str(haystack)[(position):(position+length)]


# Strip out any HTML tags found in input string
def StripHTML(data):
    data = str(data)
    p = re.compile(r'<.*?>')
    return p.sub('', data)


# Regex search
def ReSearch(haystack, needle):
	p = re.compile(needle).search(str(haystack))
	if p:
		return p.group(1)
	else:
		return None


# Converts non-English symbols for output
def ConvertSoup(input):
    result = BeautifulStoneSoup(''.join(input), convertEntities=BeautifulStoneSoup.ALL_ENTITIES)
    return result

# -- End of file -- #