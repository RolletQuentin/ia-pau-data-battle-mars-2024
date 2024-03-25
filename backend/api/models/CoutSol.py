from pydantic import BaseModel

class CoutSol(BaseModel):
    jaugeCout : int | None = None 
    pouce : str | None = None
    difficulte : list[str] | None = None