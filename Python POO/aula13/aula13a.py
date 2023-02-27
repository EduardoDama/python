from enum import Enum, auto

class directions(Enum):
    Right = auto()
    Left = auto()


def move(directionPlayer: directions):
    if not isinstance(directionPlayer, directions):
        raise ValueError('COLOQUE A DIREÇÃO CORRETA')

    print(f'Move player for {directionPlayer.name}, {directionPlayer.value}')

move(directions.Right)
move(directions(2))

