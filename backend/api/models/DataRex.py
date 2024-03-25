from pydantic import BaseModel

class DataRex(BaseModel):
    numRex :  int | None = None 
    rex : str | None = None 
    