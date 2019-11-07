from utils import convertColNumToChar
from piece import Piece

class Square:
    
    def __init__(self, x, y):
        self._occupied = False
        self._piece = None
        self._x, self._y = x, y
        self._playerType = None

    # adds a piece to the square
    def addPiece(self, piece: str, playerType: str)->None:
        self._playerType = playerType
        self._piece = Piece(piece, self._x, self._y, playerType)
        self._occupied = True

    @property
    def name (self):
        return f"{convertColNumToChar(self.x)}{self.y}"

    @property
    def _pieceName(self):
        return str(self._piece) if self._piece else ""

    def __str__(self):
        return f"{self._piece} in {self.name}"
