from pydantic import BaseModel

class LlegirUsuari(BaseModel):
    nom: str
    edat: int 
    email: int
    direccio: str
    casat: bool

    
