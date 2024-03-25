from pydantic import BaseModel
from api.models.EstimPerso import EstimPerso
from api.models.EstimGen import EstimGen
from api.models.DataRex import DataRex

class DataSolution(BaseModel):
    numSolution: int
    titre : str | None = None
    numTechnologie : int | None = None
    technologie : str | None = None 
    definition : str | None = None
    application : str | None = None
    bilanEnergie : str | None = None
    estimPerso : EstimPerso
    estimGen : EstimGen
    listRex : list[DataRex] | None = None


