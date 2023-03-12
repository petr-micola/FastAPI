from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
quotes = Scraper()


@app.get("/{matchday}")
async def read_item(matchday):
    return quotes.scrapedata(matchday)
