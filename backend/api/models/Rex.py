from pydantic import BaseModel
from typing import Optional
from api.models.Reference import Reference
from api.models.TauxMonnaie import TauxMonnaie
from api.models.Techno import Techno
from api.models.SolutionRex import SolutionRex


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
    gain_ges: float | None = None
    ratio_gain: float | None = None
    tri: float | None = None
    capex: int | None = None
    capex_periode: int | None = None
    opexrex: int | None = None
    techno1: Optional[Techno] | None = None
    techno2: Optional[Techno] = None
    techno3: Optional[Techno] = None
    code_travaux: int | None = None
    code_reseau: int | None = None
    solutions: list[SolutionRex] = []
