from pydantic import BaseModel

class Solution(BaseModel):
    num : int
    titre : str | None = None
    degre_confiance : int | None = None
    gain_monetaire : float | None = None
    gain_watt : float | None = None
    gain_co2 : float | None = None
