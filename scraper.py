from requests_html import HTMLSession
import json


class Scraper:
    def scrapedata(self, matchday):
        url = f'https://www.ligue1.com/ranking?matchDay={matchday}'
        s = HTMLSession()
        r = s.get(url)
        print(r.status_code)
        qlist = []
        quotes = r.html.find('li.GeneralStats-row')

        for q in quotes:
            item = {
                'position': quotes.index(q) + 1,
                'team': q.find('span.GeneralStats-clubName', first=True).text,
                'points': int(q.find('div.GeneralStats-item--points', first=True).text),
                'link': list(q.find('a.GeneralStats-link', first=True).absolute_links)[0]
            }
            qlist.append(item)

        jsonstring = json.dumps(qlist)
        jsonfile = open("data.json", "w")
        jsonfile.write(jsonstring)
        jsonfile.close()
