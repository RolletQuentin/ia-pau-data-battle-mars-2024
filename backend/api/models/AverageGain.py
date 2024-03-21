from pydantic import BaseModel


class AverageGain(BaseModel):
    number_of_based_solutions: int
    average_financial_gain: float
    average_energy_gain: float
    average_ges_gain: float
    average_real_gain: float
    average_real_tri: float
