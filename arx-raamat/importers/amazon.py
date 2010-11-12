# Amazon data importer
# Ando Roots 2010

from bottlenose import *
from xml.dom import minidom

# AMAZON secrets
ACCESS_KEY_ID       = 'AKIAIWSREUOEGDASEMDQ'
SECRET_ACCESS_KEY   = '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'
ASSOCIATE_TAG       = None

get_book_details = {} # Holds the responses to GetBook call
search_book_details = {} # Holds the details of a single search result


# Search for a book by a keyword.
# Returns a list containing dicts for each result
def SearchBook(search_term):
    amazon = Amazon(ACCESS_KEY_ID, SECRET_ACCESS_KEY, ASSOCIATE_TAG)
    xml = amazon.ItemSearch(SearchIndex = 'Books', ResponseGroup = 'Medium', Keywords = search_term)
    #f = open('../importers/SearchBook.xml')
    #xml = f.read()
    #f.close
    
    dom = minidom.parseString(xml)

    final_data = []
    for search_book_item in dom.getElementsByTagName('Item'):
    	
        global search_book_item
        global search_book_details
        
        addSearchDetails('Title')
        addSearchDetails('Author', True)
        addSearchDetails('ISBN')
        addSearchDetails('ASIN')
        
        
        final_data.append(search_book_details)
        search_book_details = {}
        
    return final_data


# Returns detailed information about a book
# Search by ASIN
def GetBook(ASIN):
    amazon = Amazon(ACCESS_KEY_ID, SECRET_ACCESS_KEY, ASSOCIATE_TAG)
    xml = amazon.ItemLookup(ItemId=ASIN, IdType='ASIN', ResponseGroup='ItemAttributes')
    dom = minidom.parseString(xml)
    
    # The for loop is potentially unnecessary, but I haven't found a way to remove it.
    for get_book_item in dom.getElementsByTagName('Item'):
        global get_book_item
    
    # What data to return? The argument indicates an XML tag name
    # If the tag is not found, the entry will be ignored
    addDetails('Title')
    addDetails('Author', True)
    addDetails('ISBN')
    addDetails('ASIN')
    addDetails('Edition')
    addDetails('Manufacturer')
    addDetails('ReleaseDate')
    addDetails('Studio')
    addDetails('ReadingLevel')
    
    return get_book_details


# Adds an additional return value to the GetBook query
def addDetails(tag_name, many = False):
    data = getElement(get_book_item, tag_name, many)
    if data:
        get_book_details[tag_name] = data

# Add an additional return value to the SearchBook query
def addSearchDetails(tag_name, many = False):
    data = getElement(search_book_item, tag_name, many)
    if data:
        search_book_details[tag_name] = data


# Extract element data from XML haystack
# Param many indicates that there might be multiple elements with the same name
# They are then returned as a list
def getElement(haystack, tag, many = False):
    element = haystack.getElementsByTagName(tag)
    try:
        if many :
            data = []
            i = 0
            for instance in element:
                data.append(element[i].firstChild.data)
                i += 1
            if (len(data) == 1):
                return data[0]
            else:
                return data[0] + ' <font color="red">and </font>' + data[1]
        else:
            return element[0].firstChild.data
    except IndexError, e:
        return None

# 
#print SearchBook('Alyson Noel')
# 
# for item in m:
#     for i in item:
#         print i + ' => ' + item[i]
#         print ''
# print '--------------------------------'
#GetBook('0439358078')
# for item in m:
#     for i in item:
#         print i + ' => ' + item[i]
#         print ''