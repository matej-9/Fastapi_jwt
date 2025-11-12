from fastapi import FastAPI, HTTPException
from enum import Enum
from schemas import GenreURLChoices, Band 

app = FastAPI()

BANDS = [
    {'id':1, 'name':'The Kinks', 'genre':'Rock', 'albums': [{'title': 'master of reality', 'release_date': '1971-07-21'}]},
    {'id':2, 'name':'Aphex Twin', 'genre':'Electronic'},
    {'id':3, 'name':'Wu-Tang Clan', 'genre':'Hip-Hop'},
]

@app.get("/bands")
async def bands()-> list[Band]:
    return [
        Band(**b) for b in BANDS
    ]

@app.get("/bands/{band_id}")
async def get_band(band_id: int) -> Band:
    band = next((Band(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail = 'Band not found')
    return band

@app.get("/bands/genre/{genre}")
async def genre_page(genre: GenreURLChoices) -> list[dict]:
    genres = [b for b in BANDS if b['genre'].lower() == genre.value]
    return genres

