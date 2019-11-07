from enum import Enum
from typing import List, Tuple
from enum_values import PieceEnum, PlayerEnum

class Piece:
    """
    Class that represents a BoxShogi piece
    """

    MOVE = {
    PieceEnum.d : [(1,-1), (1,0), (1,1), (0,-1), (0,1), (-1,-1), (-1,0), (-1,1)],
    PieceEnum.n : [(x,0) for x in range(1, 5)] + [(0,x) for x in range(1, 5)] + [(-x,0) for x in range(1, 5)] + [(0,-x) for x in range(1, 5)],
    PieceEnum.g : [(x,x) for x in range(1, 5)] + [(-x,-x) for x in range(1, 5)] + [(-x,x) for x in range(1, 5)] + [(x,-x) for x in range(1, 5)],
    PieceEnum.s : [(1,-1), (1,0), (0,-1), (0,1), (-1,-1), (-1,0)],
    PieceEnum.r : [(1,-1), (0,-1), (0,1), (-1,-1)],
    PieceEnum.p : [(0,-1)]
    }

    def __init__(self, pieceType: str, x: int, y: int, playerType: str):
        self._pieceType = pieceType
        self._moves = Piece.MOVE[pieceType]
        self._promoted = False
        self._playerType = playerType
        self._x = x
        self._y = y
        self._dropped = False

    @property
    def _promotionZone(self):
        return (self._y == 1 and self._playerType == PlayerEnum.LOWER) or (self._y == Board.BOARD_SIZE and self._playerType == PlayerEnum.UPPER)
        
    def getValidMoves(self):
        pass

    # returns if player is UPPER
    @property
    def _isUpper(self):
        return self._pieceType == PlayerEnum.UPPER

    #gets the actual name of the piece
    @property
    def _name(self):
        return f"{'+' if self._promoted else ''} {self._pieceType.value if self._playerType == PlayerEnum.LOWER else self._pieceType.value.upper()}"

    #promotes a piece
    def promotePiece(self):
        self._promoted = True

    #unpromotes a piece
    def unpromote_piece(self):
        self._promoted = False
    
    #drops the piece
    def dropPiece(self):
        assert(self._dropped == False)
        self._dropped = True
        pass

    def __repr__(self):
        return self._name if self._name else ""

    def __str__(self):
        return self.__repr__()



    

