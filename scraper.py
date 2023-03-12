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
                'id': quotes.index(q) + 1,
                'name': q.find('span.GeneralStats-clubName', first=True).text.strip()
            }
            qlist.append(item)

        jsonstring = json.dumps(qlist)
        jsonfile = open("data.json", "w")
        jsonfile.write(jsonstring)
        jsonfile.close()
