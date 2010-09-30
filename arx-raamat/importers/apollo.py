# -*- coding: utf-8 -*-
# Methods to get book information from apollo.ee
# Dev/maintainer: Ando Roots 2010

import re
from google.appengine.api import urlfetch
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup


# Lookup book data from Apollo.ee DB by book ID
# Input: Book ID
# Output: Dict with Apollo's info
def GetBookByID(book_id):
    apollo_url = 'http://apollo.ee/product.php/' + book_id
    soup = BeautifulSoup(urlfetch.fetch(apollo_url).content)
    data_object = soup.find('div', attrs={'class' : 'wrapRaamat'})
    article_object = soup.find('div', attrs={'class' : 'wrapArtikkel'})
    
    # If there are any editors, put them in a list. If not, leave it be.
    editors = ReSearch(data_object, r'Toimetanud (.*?)<br />')
    if editors:
    	editors = editors.split(',')
    
    # This is the main data dict
    data = {'id': book_id,
            'title': data_object.h2,
            'description': data_object.p,
            'authors': ParseAuthors(data_object),
            'date_published': FindByPosition(data_object, 'Ilmumisaasta ', 4),
            'isbn-10': FindByPosition(data_object, 'ISBN-10 ',10),
            'isbn-13': FindByPosition(data_object, 'ISBN-13 ',13),
            'publisher': ReSearch(data_object, r'Kirjastus (.*?)<br />'),
            'price_client': soup.find('span', attrs={'class' : 'tooteSoodusHind'}),
            'price_normal': soup.find('span', attrs={'class' : 'tooteHind'}),
            'series': soup.find('a', attrs={'title' : 'Veel samast sarjast'}),
            'subtitle': soup.find('h3', attrs={'style' : 'font-weight:normal;'}),
            'format': ReSearch(data_object, r'Formaat (.*?)(;|<br />)'),
            'translator': ReSearch(data_object, r'Tõlkinud (.*?)<br />'),
            'dimensions': ReSearch(data_object, r'Mõõtmed (.*?)<br />'),
            'editors': editors,
            'illustrator': ReSearch(data_object, r'Illustreerinud (.*?)<br />'),
            'number_of_pages': ReSearch(data_object, r'Lehekülgi (.*?);'),
            'img_url': 'http://apollo.ee' + article_object('img')[0]['src']}
    
    # Trouble with encoding, convert every member of data dict
    nice_data = {}
    for i in data:
        nice_data[i] = ConvertSoup(StripHTML(data[i]))
        
    return nice_data



# Search Apollo for a book. N.B! Only returns first 15 results!
# Input: String search_term
# Output: a list with nested dict-s, one for each result
def SearchBook(search_term):
    
    # Post the search and get the HTML of the result page.
    apollo_url = 'http://apollo.ee/search.php?keyword='+search_term
    soup = BeautifulSoup(urlfetch.fetch(apollo_url).content)
    result_block = soup.find('div', attrs={'class' : 'otsingTulemusRaamat'})
    
    # Since the results are poorly structured we have to split it into individual parts.
    data_objects = str(result_block).split('<div class="sisuSplitter">&nbsp;</div>')
    data = []
    for data_object in data_objects:
    	current_soup = BeautifulSoup(data_object)
    	
    	# Primary data gathering
    	current_info = {'id': ReSearch(current_soup, r'php/(.*?)"'),
    					'title': current_soup.find('a'),
    					'description': current_soup.find('p'),
    					'authors': ParseAuthors(current_soup)}
    	
    	# Get around UTF-8 problems
    	nice_current_info = {}
    	for i in current_info:
    		nice_current_info[i] = ConvertSoup(StripHTML(current_info[i]))
    	data.append(nice_current_info)
    	nice_current_info = None
    
    return str(data)

# ------------------------------ Helper functions --------------------------------- #

# Authors need special parsing - one book can have multiple authors.
def ParseAuthors(soup):
    authors = []
    for n in soup.findAll('a', attrs={'title': 'Veel sellelt autorilt'}):
        authors.append(''.join(n.renderContents()))
    if not authors:
    	return None
    else:
    	return authors


# Custom search. Get data that follows search_string in the haystack
# Example: haystack = 'Aasta 1967 talv' | needle = 'sta ' | length = 4
# 	...would return 1967
def FindByPosition(haystack, needle, length):
	position = str(haystack).find(str(needle))
	if position != -1:
		position += len(needle)
		return str(haystack)[(position):(position+length)]
	else:
		return None


# Strip out any HTML tags found in input string
def StripHTML(data):
    data = str(data)
    p = re.compile(r'<.*?>')
    return p.sub('', data)


# Regex search
def ReSearch(haystack, needle,type='str'):
	p = re.compile(needle).search(str(haystack))
	if p:
		result = p.group(1)
		if type == 'int':
			try:
				result = int(p.group(1))
			except:
				result = None
		return result
	else:
		return None


# Converts non-English symbols for output
def ConvertSoup(input):
    result = BeautifulStoneSoup(''.join(input), convertEntities=BeautifulStoneSoup.ALL_ENTITIES)
    return result.renderContents()

# -- End of file -- #