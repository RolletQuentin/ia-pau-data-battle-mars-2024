from pydantic import BaseModel

from api.models.AverageGain import AverageGain
from api.models.AverageCout import AverageCout

class EstimPerso(BaseModel):
    estimPersoGain : AverageGain 
    estimPersoCout : AverageCout