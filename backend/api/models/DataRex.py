from pydantic import BaseModel
from api.models.GainRex import GainRex
from api.models.CoutRex import CoutRex


class DataRex(BaseModel):
    numRex :  int 
    sector : str | None = None
    pays : str | None = None 
    date : str | None = None 
    cout : CoutRex 
    gain : GainRex 
    