from pydantic import BaseModel
from api.models.Reference import Reference
from api.models.TauxMonnaie import TauxMonnaie
from api.models.Techno import Techno
from api.models.Solution import Solution


class Rex(BaseModel):
    num: int
    reference: Reference
    code_public: int
    monnaie: str
    taux_monnaie: TauxMonnaie
    gain_financier: int | None = None
    code_gain_financier_periode: int | None = None
    gain_energie: int | None = None
    code_unite_energie: int | None = None
    code_periode_energie: int | None = None
    code_energie: int | None = None
    gain_ges: int | None = None
    ration_gain: float | None = None
    tri: float | None = None
    capex: int | None = None
    capex_periode: int | None = None
    operex: int | None = None
    techno1: Techno | None = None
    techno2: Techno | None = None
    techno3: Techno | None = None
    code_travaux: int | None = None
    code_reseau: int | None = None
    solutions: list[Solution] = []
