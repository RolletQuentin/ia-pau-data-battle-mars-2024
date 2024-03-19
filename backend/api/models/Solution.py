from pydantic import BaseModel

class Solution(BaseModel):
    num : int
    titre : str | None = None
    degre_confiance : int | None = None
    gain_monetaire : str | None = None
    gain_watt : str | None = None
    gain_co2 : str | None = None
