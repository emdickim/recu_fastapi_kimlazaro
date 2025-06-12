from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os
from Models.usuaris import usuari
from services.usuari import crear_usuari
from fastapi import Depends
from typing import Generator

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