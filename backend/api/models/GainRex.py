from pydantic import BaseModel


class GainRex(BaseModel):
    num: int
    code_solution: int
    code_rex: int
    gain_financier: int | None = None
    monnaie: str | None = None
    code_periode_economie: int | None = None
    gain_energie: int | None = None
    unite_energie: int | None = None
    code_periode_energie: int | None = None
    gain_ges: int | None = None
    gain_reel: float | None = None
    tri_reel: int | None = None
