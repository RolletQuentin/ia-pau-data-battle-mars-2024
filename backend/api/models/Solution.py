from pydantic import BaseModel

from api.models.AverageGain import AverageGain
from api.models.AverageCout import AverageCout

class Solution(BaseModel):
    num : int
    titre : str | None = None
    estimPersoGain :  AverageGain
    estimPersoCout : AverageCout
    codeSector : int
