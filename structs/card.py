from dataclasses import dataclass
from enum import Enum, auto


class CardType(Enum):
    HEARTS = auto()
    SPADES = auto()
    DIAMONDS = auto()
    CLUBS = auto()


@dataclass
class Card:
    number: int
    type: CardType
