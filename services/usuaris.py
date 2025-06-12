from Models.usuaris import usuari
from sqlmodel import Session


def usuari_per_id(usuari_id: int, db: Session):
    return db.get(usuari, usuari_id)

def crear_usuari(Usuari: usuari, db: Session):
    db.add(Usuari)
    db.commit()
    db.refresh(Usuari)
    return Usuari


def update_user(usuari_id: int, nou_valor: usuari, db: Session):
    db_usuari = db.get(usuari, usuari_id)
    if not db_usuari:
        return None
    for key, value in nou_valor.dict(exclude_unset=True).items():
        setattr(db_usuari, key, value)
    db.commit()
    db.refresh(db_usuari)
    return db_usuari


def delete_usuari(usuari_id: int, db: Session):
    Usuari = db.get(usuari, usuari_id)
    if not Usuari:
        return False
    db.delete(Usuari)
    db.commit()
    return True
