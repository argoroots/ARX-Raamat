from bottlenose import *


ACCESS_KEY_ID       = 'AKIAIWSREUOEGDASEMDQ'
SECRET_ACCESS_KEY   = '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'
ASSOCIATE_TAG       = None


def AmazonBookSearch(search_term):
    amazon = Amazon(ACCESS_KEY_ID, SECRET_ACCESS_KEY, ASSOCIATE_TAG)
    xml = amazon.ItemSearch(SearchIndex = 'Books', ResponseGroup = 'Medium', Keywords = search_term)

    return xml