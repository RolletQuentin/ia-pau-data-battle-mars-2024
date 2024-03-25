from pydantic import BaseModel

from api.models.CoutSol import CoutSol
from api.models.GainSol import GainSol

class EstimGen(BaseModel):
    cout : CoutSol
    gain : GainSol