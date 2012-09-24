from bo import *
from database.person import *


class ShowGroup(boRequestHandler):
    def get(self, url):

        group = url.strip('/')
        if not group:
            self.redirect('/persons/debtors')
            return

        groups = db.Query(Group)
        groups.filter('library', Person().current.current_library)
        groups.order('name')
        groups.fetch(1000)

        persons = db.Query(Person)
        persons.filter('library', Person().current.current_library)
        if group == 'staff':
            persons.filter('type IN', ['staff', 'admin'])
        elif group == 'deptors':
            persons.filter('type IN', ['staff', 'admin'])
        else:
            if group:
                persons.filter('group', db.Key.from_path('Group', group))
        persons.order('forename')
        persons.order('surname')
        persons.fetch(1000)

        self.view('', 'person/persons.html', {
            'groups': groups,
            'persons': persons,
            'selected': group,
        })


class ShowPerson(boRequestHandler):
    def get(self, url):
        pass


def main():
    Route([
             (r'/persons(.*)', ShowGroup),
             (r'/person(.*)', ShowPerson),
            ])


if __name__ == '__main__':
    main()