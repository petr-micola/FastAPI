import json

from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
quotes = Scraper()


@app.get("/{matchday}")
async def read_item(matchday):
    quotes.scrapedata(matchday)
    j = open('data.json')
    jsondata = json.load(j)
    j.close()
    return jsondata
