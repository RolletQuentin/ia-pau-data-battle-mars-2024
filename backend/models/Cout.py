from pydantic import BaseModel


class Cout(BaseModel):
    num: int
    cout_reel: int | None = None
    monnaie: str
