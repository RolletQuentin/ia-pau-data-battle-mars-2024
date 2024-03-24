from pydantic import BaseModel


class Monnaie(BaseModel):
    num: int
    short_monnaie: str | None = None
    valeur_taux: float | None = None
