from enum import Enum
from typing import List, Tuple
from enum_values import PieceEnum, PlayerEnum
from utils import *

class Piece:
    """
    Class that represents a BoxShogi piece
    """

    # Regular moves in 
    MOVE = {
        PieceEnum.d : [(1,-1), (1,1), (-1,-1), (-1,1), (1,0), (0,-1), (0,1), (-1,0)],
        PieceEnum.n : [(x,0) for x in range(1, 5)] + [(0,x) for x in range(1, 5)] + [(-x,0) for x in range(1, 5)] + [(0,-x) for x in range(1, 5)],
        PieceEnum.g : [(x,x) for x in range(1, 5)] + [(-x,-x) for x in range(1, 5)] + [(-x,x) for x in range(1, 5)] + [(x,-x) for x in range(1, 5)],
        PieceEnum.s : [(1,1), (-1,1), (1,0), (0,1), (0,-1), (-1,0)],
        PieceEnum.r : [(1,1), (-1,1), (-1,-1), (1,-1), (0,1)],
        PieceEnum.p : [(0, 1)]
    }

    # Moves that come when promoted    
    PMOVE = {        
        PieceEnum.n : MOVE[PieceEnum.n] + [(1,1), (1,-1), (-1,1),(-1,-1)],
        PieceEnum.g : MOVE[PieceEnum.g] + [(0,1), (-1, 0), (0,-1), (1,0)],
        PieceEnum.r : MOVE[PieceEnum.s],
        PieceEnum.p : MOVE[PieceEnum.s]
    }

    def __init__(self, pieceType: str, x: int, y: int, playerType: str, captured=False):
        self._pieceType = pieceType
        self._moves = Piece.MOVE[pieceType]
        self._promoted = False
        self._playerType = playerType
        self._x = x
        self._y = y
        self._captured = captured

    @property
    def _promotionZone(self):
        return (self._y == 1 and self._playerType == PlayerEnum.LOWER) or (self._y == Board.BOARD_SIZE and self._playerType == PlayerEnum.UPPER)

    @property
    def _coord(self):
        return (self._x, self._y)
        
    def getValidMoves(self, squares, ignoreSide=False):

        valid_moves = []
        currentMoves = self._moves if self._playerType == PlayerEnum.LOWER else list(map(lambda x: (x[0], x[1] * -1), self._moves))

        # used to protect against jumpings
        directionalMagnitude = 10

        for dx, dy in currentMoves:
            nextX = self._x + dx
            nextY = self._y + dy

            # if self._pieceType == PieceEnum.s:
            #     print('parsed', (nextX, nextY), abs(dx) + abs(dy))

            if oob(nextX, nextY) or abs(dx) + abs(dy) > directionalMagnitude:
                # if self._pieceType == PieceEnum.s:
                    # print((nextX, nextY), abs(dx) + abs(dy))
                continue

            else:
                directionalMagnitude = 10
            
                # if self._pieceType == PieceEnum.s:
                #     print((nextX, nextY))

            # subtract one because our squares are 0 indexed
            relevantSquare = squares[nextX-1][nextY-1]
            
            if relevantSquare.hasPiece() and relevantSquare._piece._pieceType != PieceEnum.d:
                directionalMagnitude = abs(dx) + abs(dy) 
                
                if relevantSquare._piece._playerType == self._playerType and not ignoreSide:
                    continue

            # we passed these checks, so we move on 
            valid_moves.append((nextX, nextY))

        # print(self._pieceType, valid_moves)

        return valid_moves


    # returns if player is UPPER
    @property
    def _isUpper(self):
        return self._playerType == PlayerEnum.UPPER

    #gets the actual name of the piece
    @property
    def _name(self):
        return f"{'+' if self._promoted else ''}{self._pieceType.value if self._playerType == PlayerEnum.LOWER else self._pieceType.value.upper()}"

    #promotes a piece
    def promotePiece(self):
        self._promoted = True
        self._moves = Piece.PMOVE[self._pieceType]

    #unpromotes a piece
    def unpromote_piece(self):
        self._promoted = False
        self._moves = Piece.MOVE[self._pieceType]
    
    #drops the piece
    def capturePiece(self, playerType):
        self._playerType = playerType
        self._captured = True 
    
    def movePiece(self, x: int, y: int):
        self._x = x
        self._y = y

    def __repr__(self):
        return self._name if self._name else ""

    def __str__(self):
        return self.__repr__()



    

