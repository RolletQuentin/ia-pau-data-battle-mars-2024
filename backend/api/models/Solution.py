from pydantic import BaseModel

from api.models.Cout import Cout
from api.models.Gain import Gain


class Solution(BaseModel):
    num: int
    couts: list[Cout] = []
    gains: list[Gain] = []
