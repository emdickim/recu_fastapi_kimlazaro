from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os
from Models.usuaris import usuari
from services.usuaris import crear_usuari
from fastapi import Depends
from typing import Generator
from services.usuaris import usuari_per_id

from schema.usuari import LlegirUsuari
=======


app = FastAPI()


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


SQLModel.metadata.create_all(engine)


def get_db():
   db = Session(engine)
   try:
       yield db
   finally:
       db.close()


@app.post("/usuaris/")
def crear_usuari(usuaris: usuari, db: Generator = Depends(get_db)):

    return crear_usuari(usuari, db)




@app.get("/usuaris/{usuari_id}", response_model=LlegirUsuari)

@app.get("/usuaris/{usuari_id}")

def read_usuari(usuari_id: int, db: Generator = Depends(get_db)):
    usuari = usuari_per_id(usuari_id, db)
    if not usuari:
        return {"error": "Usuari no trobat"}
    return usuari