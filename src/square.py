from utils import convertColNumToChar
from piece import Piece


class Square:
    
    def __init__(self, x, y):
        self._occupied = False
        self._piece = None
        self._x, self._y = x, y
        self._coord = (x,y)
        

    # adds a piece to the square
    def addPiece(self, piece: str, playerType: str)-> None:
        self._piece = Piece(piece, self._x, self._y, playerType)
        self._occupied = True

    @property
    def _playerType(self):
        return None if not self._piece else self._piece._playerType

    def hasPiece(self):
        return self._piece != None
    
    # similar to add, except we already have a piece here
    def placePiece(self, piece: Piece):   
        piece.movePiece(self._x, self._y)
        self._piece = piece
        self._occupied = True

    # sets piece to none
    def removePiece(self, drop = False, player=None):

        assert(self._piece != None)

        if drop:
            self._piece.unpromote_piece()
            self._piece.dropPiece(player._playerType)
            player.addCapture(self._piece)

        self._piece = None


    #returns if in promotion zone
    def inPromotionZone(self):
        if not self.hasPiece():
            return False
        
        return (self._y == 1 and piece._isUpper) or (self._y == 5 and not piece._isUpper)

    
    @property
    def name (self):
        return f"{convertColNumToChar(self._x)}{self._y}"

    @property
    def _pieceName(self):
        return str(self._piece) if self._piece else ""

    def __str__(self):
        return f"{self._piece} in {self.name}"
