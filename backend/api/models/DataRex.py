from pydantic import BaseModel
from api.models.GainRex import GainRex
from api.models.CoutRex import CoutRex


class DataRex(BaseModel):
    numRex :  int | None = None
    sector : str | None = None
    cout : list[CoutRex]
    gain : list[GainRex]
    