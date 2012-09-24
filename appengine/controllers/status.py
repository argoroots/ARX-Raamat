from google.appengine.api.capabilities import *

from bo import *


class ShowStatus(boRequestHandler):
    def get(self):

        services = []
        services.append({'name': 'Blobstore',       'status': CapabilitySet('blobstore').is_enabled()})
        #services.append({'name': 'Datastore',       'status': CapabilitySet('datastore').is_enabled()})
        #services.append({'name': 'Datastore write', 'status': CapabilitySet('datastore_write').is_enabled()})
        services.append({'name': 'Images',          'status': CapabilitySet('images').is_enabled()})
        services.append({'name': 'Mail',            'status': CapabilitySet('mail').is_enabled()})
        services.append({'name': 'Memcache',        'status': CapabilitySet('memcache').is_enabled()})
        services.append({'name': 'Taskqueue',       'status': CapabilitySet('taskqueue').is_enabled()})
        #services.append({'name': 'URL fetch',       'status': CapabilitySet('url_fetch').is_enabled()})
        services.append({'name': 'XMPP',            'status': CapabilitySet('xmpp').is_enabled()})

        self.view('app_status', 'status.html', {
            'services': services
        })


def main():
    Route([
             ('/status', ShowStatus),
            ])


if __name__ == '__main__':
    main()