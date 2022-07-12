from dataclasses import dataclass
from typing import List
from enum import Enum, auto

from structs.card import Card


class SeriesType(Enum):
    ASCENDING = auto()
    DESCENDING = auto()
    COLOR = auto()


@dataclass
class Series:
    cards: List[Card]
    type: SeriesType
