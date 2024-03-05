from pydantic import BaseModel

from models.Cout import Cout
from models.Gain import Gain


class Solution(BaseModel):
    num: int
    couts: list[Cout] = []
    gains: list[Gain] = []
