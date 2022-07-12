from dataclasses import dataclass
from typing import List

from structs.series import Series


@dataclass
class Board:
    # TODO: singleton
    cards: List[Series]
