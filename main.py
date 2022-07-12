from structs.card import *
from structs.series import *
from structs.board import *


# TODO: tests

def main():
    c1 = Card(number=3, type=CardType.SPADES)
    c2 = Card(number=4, type=CardType.SPADES)
    c3 = Card(number=2, type=CardType.SPADES)
    s1 = Series(type=SeriesType.STAIRS, cards=[c1, c2, c3])
    b1 = Board(series=[s1])
    print(b1)


if __name__ == '__main__':
    main()
