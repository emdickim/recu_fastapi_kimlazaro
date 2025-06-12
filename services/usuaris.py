from Models.usuaris import usuari
from sqlmodel import Session


def usuari_per_id(usuari_id: int, db: Session):
    return db.get(usuari, usuari_id)

def crear_usuari(Usuari: usuari, db: Session):
    db.add(Usuari)
    db.commit()
    db.refresh(Usuari)
    return Usuari