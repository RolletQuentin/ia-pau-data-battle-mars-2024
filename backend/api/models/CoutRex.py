from pydantic import BaseModel

from api.models.Monnaie import Monnaie


class CoutRex(BaseModel):
    code_rex: int | None = None 
    num: int | None = None 
    code_solution:  int | None = None 
    text: str | None = None 
    cout_reel: float | None = None 
    monnaie: Monnaie | None = None 
    code_unite_cout: int | None = None
    code_difficulte: int | None = None
    code_secteur: int | None = None
