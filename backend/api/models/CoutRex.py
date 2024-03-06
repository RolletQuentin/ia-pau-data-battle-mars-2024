from pydantic import BaseModel


class CoutRex(BaseModel):
    num: int
    code_solution: int
    code_rex: int
    cout_reel: int | None = None
    monnaie: str | None = None
    code_unite_cout: int | None = None
    code_difficulte: int | None = None
