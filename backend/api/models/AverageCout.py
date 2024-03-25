from pydantic import BaseModel


class  AverageCout(BaseModel):
    number_of_based_solutions: int
    average_cout: float | None = None
