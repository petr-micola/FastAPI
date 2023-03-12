from requests_html import HTMLSession
import json


class Scraper:
    def scrapedata(self):
        url = f'https://www.ligue1.com/ranking'
        s = HTMLSession()
        r = s.get(url)

        data = r.html.find('li.GeneralStats-row')

        dlist = []

        for d in data:
            item = {
                'id': data.index(d),
                'team': d.find('span.GeneralStats-clubName', first=True).text,
                'points': int(d.find('div.GeneralStats-item--points', first=True).text),
                'link': list(d.find('a.GeneralStats-link', first=True).absolute_links)[0]
            }
            dlist.append(item)

        j = open('data.json', 'w')
        j.write(json.dumps(dlist))
        j.close()
