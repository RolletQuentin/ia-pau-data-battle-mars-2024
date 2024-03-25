from pydantic import BaseModel

class GainSol(BaseModel):
    jaugeGain : int | None = None 
    gain : str | None = None 
    positif : list[str] | None = None