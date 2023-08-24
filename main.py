from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from sqlmodel import Session, select
from db_engine.connection import Artist_Model, engine



app = FastAPI()



class Artist(BaseModel):
    name: str
    email: str | None = None
    age: int | None = None

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.post("/artists/")
async def create_artist(artist: Artist):
    new_artist = Artist_Model(name=artist.name, email=artist.email, age=artist.age)
    try:
        with Session(engine) as session:
            session.add(new_artist)
            session.commit()
    except Exception:
        return "Error creating artist"
    return new_artist

@app.get("/artists/{artist_id}")
def read_artist_id(artist_id: int):
    try:
        with Session(engine) as session:
            statement = select(Artist_Model).where(Artist_Model.id == artist_id)
            result_artist = session.exec(statement).first()
        return result_artist
    except:
        "wrong artist id"

