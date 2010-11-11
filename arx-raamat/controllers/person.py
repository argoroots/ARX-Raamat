from bo import *
from database import *


class ShowStaff(webapp.RequestHandler):
    def get(self):

        groups = db.Query(Group)
        groups.filter('library', Person().current.library)
        groups.order('name')
        groups.fetch(100)

        persons = db.Query(Person)
        persons.filter('library', Person().current.library)
        persons.filter('status', 'normal')
        persons.filter('type IN', ['staff', 'admin'])
        persons.order('forename')
        persons.order('surname')
        persons.fetch(1000)

        View(self, '', 'person.html', {
            'groups': groups,
            'persons': persons,
            'selected': 'staff',
        })


class ShowDebtors(webapp.RequestHandler):
    def get(self):
        pass


class ShowGroup(webapp.RequestHandler):
    def get(self, url):

        url = url.strip('/')

        groups = db.Query(Group)
        groups.filter('library', Person().current.library)
        groups.order('name')
        groups.fetch(100)

        persons = db.Query(Person)
        persons.filter('library', Person().current.library)
        persons.filter('status', 'normal')
        persons.filter('group', Group().get_by_id(int(url[1])))
        persons.order('forename')
        persons.order('surname')
        persons.fetch(1000)

        View(self, '', 'person.html', {
            'groups': groups,
            'persons': persons,
            'selected': url,
        })


class ShowPerson(webapp.RequestHandler):
    def get(self, url):

        url = url.strip('/')

        groups = db.Query(Group)
        groups.filter('library', Person().current.library)
        groups.order('name')
        groups.fetch(100)

        persons = db.Query(Person)
        persons.filter('library', Person().current.library)
        persons.filter('status', 'normal')
        #persons.filter('group', Group().get_by_id(int(url[1])))
        persons.order('forename')
        persons.order('surname')
        persons.fetch(1000)

        View(self, '', 'person.html', {
            'groups': groups,
            'persons': persons,
            'selected': url,
        })


def main():
    Route([
             ('/person/staff', ShowStaff),
             ('/person/debtors', ShowDebtors),
             (r'/person/group(.*)', ShowGroup),
             (r'/person(.*)', ShowPerson),
            ])


if __name__ == '__main__':
    main()