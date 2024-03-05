from pydantic import BaseModel
from models.Region import Region
from models.Techno import Techno


class Reference(BaseModel):
    num: int
    region: Region
    ville_reference: str | None = None
    techno: Techno | None = None
    code_secteur: int | None = None
    is_recup_chaleur: bool
