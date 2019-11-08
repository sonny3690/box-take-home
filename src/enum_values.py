from enum import Enum, unique

# Player Enums
class PlayerEnum(Enum):
    LOWER = 'lower'
    UPPER = 'UPPER'

# Piece Enums
class PieceEnum(Enum):
    d = 'd'
    n = 'n'
    g = 'g'
    s = 's'
    r = 'r'
    p = 'p'

class GameState(Enum):
    PLAYING = 'PLAYING'
    LOWER_WIN = 'LOWER_WIN'
    UPPER_WIN = 'UPPER_WIN'
    TIE = 'TIE'

class MoveType(Enum):
    MOVE = 'move'
    DROP = 'drop'
