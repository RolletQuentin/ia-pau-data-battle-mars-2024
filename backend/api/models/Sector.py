from typing import List, Dict
from pydantic import BaseModel



class Sector(BaseModel):
    sectors: Dict[str, List[str]]