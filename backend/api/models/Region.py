from pydantic import BaseModel


class Region(BaseModel):
    num: int
    code_pays: int
    national_region: bool
    latitude: float
    longitude: float
