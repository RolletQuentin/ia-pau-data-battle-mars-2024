from pydantic import BaseModel

from api.models.Monnaie import Monnaie


class GainRex(BaseModel):
    num: int | None = None
    code_solution: int
    code_rex: int
    gain_financier: float | None = None
    monnaie: Monnaie | None = None
    code_periode_economie: int | None = None
    gain_energie: float | None = None
    unite_energie: int | None = None
    code_periode_energie: int | None = None
    gain_ges: float | None = None
    gain_reel: float | None = None
    tri_reel: float | None = None
    nom_periode_energie: str | None = None
    nom_unite_energie: str | None = None
    nom_periode_economie: str | None = None
    code_secteur: int | None = None
