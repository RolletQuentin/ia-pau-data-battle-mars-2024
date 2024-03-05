from pydantic import BaseModel


class Cout(BaseModel):
    num: int
    cout_reel: int | None = None
    monnaie: str | None = None
    code_unite_cout: int | None = None
    code_difficulte: int | None = None
