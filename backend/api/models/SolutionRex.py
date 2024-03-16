from pydantic import BaseModel

from api.models.CoutRex import CoutRex
from api.models.GainRex import GainRex


class SolutionRex(BaseModel):
    num: int
    couts: list[CoutRex] = []
    gains: list[GainRex] = []
