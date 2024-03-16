from pydantic import BaseModel
from typing import Optional
from api.models.Region import Region
from api.models.Techno import Techno


class Reference(BaseModel):
    num: int
    region: Region
    ville_reference: str | None = None
    techno: Optional[Techno] = None
    code_secteur: int | None = None
    is_recup_chaleur: bool
