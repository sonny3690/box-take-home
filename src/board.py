import os
from enum_values import PlayerEnum, PieceEnum
from square import Square

class Board:
    """
    Class that represents the BoxShogi board
    """

    # The BoxShogi board is 5x5
    BOARD_SIZE = 5
    INITIAL_ARRANGEMENT = [(PieceEnum.n, 0, 0),  (PieceEnum.g, 1, 0), (PieceEnum.r, 2, 0), (PieceEnum.s, 3, 0), (PieceEnum.d, 4, 0), (PieceEnum.p, 4, 1)]

    def __init__(self):
        self._board = self._initEmptyBoard()
        self.addInitialPieces()

    #adds some pieces, takes None, returns None
    def addInitialPieces(self) -> None:
        for piece, dx, dy in Board.INITIAL_ARRANGEMENT:
            self._board[dx][Board.BOARD_SIZE-1-dy].addPiece(piece, PlayerEnum.UPPER)
            self._board[Board.BOARD_SIZE-dx-1][dy].addPiece(piece, PlayerEnum.LOWER)

    # initializes an empty board        
    def _initEmptyBoard(self):
        #creates a bunch of squares and saves it in a list
        return [[Square(x,y) for y in range(1, self.BOARD_SIZE+1)] for x in range(1, self.BOARD_SIZE+1)]
    
    def _getBoard(self, x: int, y: int)->Square:
        return self._board[x-1][y-1]

        
    def __repr__(self):
        return self._stringifyBoard()

    def _stringifyBoard(self):
        """
        Utility function for printing the boards
        """
        s = ''
        for row in range(len(self._board) - 1, -1, -1):

            s += '' + str(row + 1) + ' |'
            for col in range(0, len(self._board[row])):
                s += self._stringifySquare(self._board[col][row]._pieceName)

            s += os.linesep

        s += '    a  b  c  d  e' + os.linesep
        return s

    def _stringifySquare(self, sq):
        """
       	Utility function for stringifying an individual square on the board

        :param sq: Array of strings.
        """

        if type(sq) is not str or len(sq) > 2:
            raise ValueError('Board must be an array of strings like "", "P", or "+P"')
        if len(sq) == 0:
            return '__|'
        if len(sq) == 1:
            return ' ' + sq + '|'
        if len(sq) == 2:
            return sq + '|'