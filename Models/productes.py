from sqlmodel import SQLModel, Field

class usuari(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    preu: float
    enStoc: str
    marca: str
    descripcio: str
