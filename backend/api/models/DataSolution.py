from pydantic import BaseModel
from api.models.AverageGain import AverageGain
from api.models.AverageCout import AverageCout
#from api.models.DataRex import DataRex

class DataSolution(BaseModel):
    num: int
    titre : str | None = None
    technologie : str | None = None
    definition : str | None = None
    application : str | None = None
    bilanEnergie : str | None = None
    estimPersoGain : AverageGain 
    estimGenGain : AverageCout
    #dataRex : DataRex

