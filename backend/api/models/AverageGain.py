from pydantic import BaseModel


class AverageGain(BaseModel):
    number_of_based_solutions: int
    average_financial_gain: float | None = None
    average_energy_gain: float | None = None
    average_ges_gain: float | None = None
    average_real_gain: float | None = None
    average_real_tri: float | None = None
