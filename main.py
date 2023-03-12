import json

from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
s = Scraper()


@app.get('/ranking')
async def read_items():
    s.scrapedata()
    j = open('data.json', 'r')
    data = json.load(j)
    j.close()
    return data


@app.get('/ranking/{id}')
async def read_item(id):
    s.scrapedata()
    j = open('data.json', 'r')
    data = json.load(j)
    j.close()
    return data[int(id)]
