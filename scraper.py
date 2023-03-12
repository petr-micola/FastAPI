from requests_html import HTMLSession


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
                'name': q.find('span.GeneralStats-clubName', first=True).text.strip()
            }
            print(item)
            qlist.append(item)

        return qlist
