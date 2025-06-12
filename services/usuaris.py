from Models.usuaris import usuari
from sqlmodel import Session

def crear_usuari(Usuari: usuari, db: Session):
    db.add(Usuari)
    db.commit()
    db.refresh(Usuari)
    return Usuari