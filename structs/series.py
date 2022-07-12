from pydantic import BaseModel, validator
from typing import List
from enum import Enum, auto

from structs.card import Card


class SeriesType(Enum):
    STAIRS = auto()
    TYPE = auto()


class Series(BaseModel):
    type: SeriesType
    cards: List[Card]

    @validator('cards')
    def validate_cards(cls, v, values):
        if len(v) < 3:
            raise ValueError('Series must be at least 3 cards long')

        series_type = values['type']
        if series_type == SeriesType.TYPE:
            if len(set(c.type for c in v)) != len(v):
                raise ValueError('Type series can not contain the same type twice')
            if not all(v[0].number == c.number for c in v[1:]):
                raise ValueError('Type series can not contain different numbers')
            return sorted(v, key=lambda c: c.type.value)
        if series_type == SeriesType.STAIRS:
            if not all(v[0].type == c.type for c in v[1:]):
                raise ValueError('Type must be unique throughout a stairs series')
            sorted_cards = sorted(v, key=lambda c: c.number)
            sorted_numbers = [c.number for c in sorted_cards]
            if sorted_numbers != list(range(sorted_numbers[0], sorted_numbers[-1] + 1)):
                raise ValueError('Series is missing or doubling some steps')
            return sorted_cards
