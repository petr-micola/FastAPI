from fastapi import FastAPI
from pydantic import BaseModel
import json

from scraper import Scraper

app = FastAPI()
s = Scraper()
s.scrapedata()


class Item(BaseModel):
    id: int
    team: str
    points: int
    link: str


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/ranking')
async def read_items():
    j = open('data.json', 'r')
    data = json.load(j)
    j.close()
    return data


@app.get('/ranking/{item_id}')
async def read_item(item_id: int):
    j = open('data.json', 'r')
    data = json.load(j)
    j.close()
    return data[int(item_id)]


@app.post('/ranking/')
async def add_item(item: Item):
    j = open('data.json', 'r')
    data = json.load(j)
    data.append(dict(item))
    j.close()

    j = open('data.json', 'w')
    j.write(json.dumps(data))
    j.close()

    return item
