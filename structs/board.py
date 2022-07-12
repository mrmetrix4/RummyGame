from pydantic import BaseModel
from typing import List

from structs.series import Series


class Board(BaseModel):
    # TODO: singleton
    series: List[Series]
