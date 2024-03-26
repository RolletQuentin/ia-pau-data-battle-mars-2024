from pydantic import BaseModel

from api.models.Content import Content
from api.models.EstimPerso import EstimPerso
from api.models.EstimGen import EstimGen
from api.models.DataRex import DataRex

class DataSolution(BaseModel):
    numSolution: int
    titre : str | None = None
    numTechnologie : int | None = None
    technologie : str | None = None 

    definition : list[Content] | None = None

    application : list[Content] | None = None

    bilanEnergie : list[Content] | None = None

    estimPerso : EstimPerso
    estimGen : EstimGen
    listRex : list[DataRex] | None = None


