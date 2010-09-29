# -*- coding: utf-8 -*-
# Methods to get book information from apollo.ee
# Dev/maintainer: Ando Roots 2010

import os
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
    
    # Authors need special parsing - one book can have multiple authors.
    authors = []
    for n in data_object.findAll('a', attrs={'title': 'Veel sellelt autorilt'}):
        authors.append(''.join(n.findAll(text=True)))

    # Date published
    position = str(data_object).find('Ilmumisaasta')+12
    date_published = str(data_object)[(position+1):(position+5)]
    
    # ISBN
    position = str(data_object).find('ISBN-13')+8
    isbn = str(data_object)[(position):(position+13)]
    
    # This is the main data dict
    data = {'ID': book_id,
            'title': data_object.h2,
            'description': data_object.p,
            'authors': authors,
            'date_published': date_published,
            'isbn': isbn}
    
    # Trouble with unicode, UTF-8
    nice_data = {}
    for i in data:
        nice_data[i] = ConvertSoup(StripHTML(data[i]))
        
    return nice_data

# Strip out any HTML tags found in input string
def StripHTML(data):
    data = str(data)
    p = re.compile(r'<.*?>')
    return p.sub('', data)
    
# Converts non-English symbols for output
def ConvertSoup(input):
    result = BeautifulStoneSoup(''.join(input), convertEntities=BeautifulStoneSoup.ALL_ENTITIES)
    return result