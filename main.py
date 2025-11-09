from fastapi import FastAPI, HTTPException
from enum import Enum


app = FastAPI()

class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    HIP_HOP = 'hip-hop'

BANDS = [
    {'id':1, 'name':'The Kinks', 'genre':'Rock'},
    {'id':2, 'name':'Aphex Twin', 'genre':'Electronic'},
    {'id':3, 'name':'Wu-Tang Clan', 'genre':'Hip-Hop'},
]

@app.get("/bands")
async def bands()-> list[dict]:
    return BANDS

@app.get("/bands/{band_id}")
async def get_band(band_id: int) -> dict:
    band = next((b for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail = 'Band not found')
    return band

@app.get("/bands/genre/{genre}")
async def genre_page(genre: GenreURLChoices) -> list[dict]:
    genres = [b for b in BANDS if b['genre'].lower() == genre.value]
    return genres

