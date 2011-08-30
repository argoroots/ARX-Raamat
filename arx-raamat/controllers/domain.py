from bo import *
from google.appengine.api import urlfetch
from importers.BeautifulSoup import BeautifulSoup


class CheckDomains(webapp.RequestHandler):
    def get(self, url):

        domains = [
            #'aa',
            #'animaster',
            #'apple',
            #'artun',
            #'arx',
            #'eaa',
            #'emug',
            #'ka',
            #'kogu',
            #'mac',
            #'portfoolio',
            #'roots',
            #'saal',
            #'tants',
            #'ww',
            'eka',
            'raamat',
            'raamatukogu',
        ]
        registered = []
        unregistered = []

        self.response.headers['Content-Type'] = 'text/plain'

        for domain in domains:
            url = 'https://www.zone.ee/et/domeeni-otsing?cat=domainStatus&ext=ee&rdomain=' + domain
            content = urlfetch.fetch(url, deadline=10).content
            soup = BeautifulSoup(content)

            div = soup.find('div', attrs={'class' : 'whois_status_box'})
            div = str(div.find('blockquote'))
            #self.response.out.write(div)
            div = div[div.find('registrant'):][:div.find('<br />')].split(':')[2]

            if div == 'EEDIRECT':
                unregistered.append(domain)
            else:
                registered.append(domain)

        self.response.out.write('- registered:\n  ')
        self.response.out.write('\n  '.join(registered))
        self.response.out.write('\n')
        self.response.out.write('\n')
        self.response.out.write('- unregistered:\n  ')
        self.response.out.write('\n  '.join(unregistered))


def main():
    Route([
             (r'/domain(.*)', CheckDomains),
            ])


if __name__ == '__main__':
    main()