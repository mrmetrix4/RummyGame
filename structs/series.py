from pydantic import BaseModel
from typing import List
from enum import Enum, auto

from structs.card import Card


class SeriesType(Enum):
    ASCENDING = auto()
    DESCENDING = auto()
    COLOR = auto()


class Series(BaseModel):
    cards: List[Card]
    type: SeriesType
