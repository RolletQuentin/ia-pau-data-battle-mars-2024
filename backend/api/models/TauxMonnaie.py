from pydantic import BaseModel


class TauxMonnaie(BaseModel):
    num: int
    monnaie: str
    annee: int
    valeur_taux: float
