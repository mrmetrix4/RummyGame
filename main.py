from structs.card import *
from structs.series import *
from structs.board import *


def main():
    c1 = Card(number=1, type=CardType.HEARTS)
    s1 = Series(cards=[c1], type=SeriesType.COLOR)
    b1 = Board(series=[s1])
    print(b1)


if __name__ == '__main__':
    main()
