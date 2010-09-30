# -*- coding: utf-8 -*-
# A Cron test for Apollo importer that runs once a day.
# Check if Apollo has changed it's HTML structure wich would mean the importer is broken.
# Idea - store importer data in GQL so it would be possible to disable the importer when needed

import pickle
import hashlib
from bo import *
from importers.apollo import *

class ApolloCronTest(webapp.RequestHandler):
    def get(self, param):
        
        # I know something about those 4 books. If my info is not the same as Apollo's response
        # ...and it is so with all 4 of them, then it's a good guess the admin needs to check the syntax manually.
        
        # Pickle it - make dict a string
        result1 = pickle.dumps(set(GetBookByID('0722492').items())) # Videvik
        result2 = pickle.dumps(set(GetBookByID('0761862').items())) # Musta pori nakku
        result3 = pickle.dumps(set(GetBookByID('0305224').items())) # HP 7
        result4 = pickle.dumps(set(GetBookByID('3289239').items())) # Hobevalge
        
        # MD5 it - make a long string short
        result1 = hashlib.md5(result1).hexdigest()
        result2 = hashlib.md5(result2).hexdigest()
        result3 = hashlib.md5(result3).hexdigest()
        result4 = hashlib.md5(result4).hexdigest()
        
        # These are the saved MD5 values. N.B! If something in apollo.py output dict is changed these MUST BE updated.
        stored1 = ''
        stored2 = ''
        stored3 = ''
        stored4 = ''
        
        self.response.out.write((result1, result2, result3, result4))
        
        # Notify admins about system failure.
        if result1 != stored1 or result2 != stored2 or result3 != stored3 or result4 != stored4:
            #SendMail('ando@roots.ee',Translate('apollo_failure_msg_title'), Translate('apollo_failure_msg'))
            a=3
        self.response.out.write('<br />1')
        

def main():
    Route([
             ('/apollo_cron/(.*)', ApolloCronTest),
            ])


if __name__ == '__main__':
    main()