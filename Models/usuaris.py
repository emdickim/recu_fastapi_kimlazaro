from sqlmodel import SQLModel, Field


class usuari(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nom: str
    edat: int 
    email: int
    direccio: str
    casat: bool