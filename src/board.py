import os
from enum_values import PlayerEnum, PieceEnum
from square import Square
from utils import coordStringToCoord

class Board:
    """
    Class that represents the BoxShogi board
    """

    # The BoxShogi board is 5x5
    BOARD_SIZE = 5
    INITIAL_ARRANGEMENT = [(PieceEnum.n, 0, 0),  (PieceEnum.g, 1, 0), (PieceEnum.r, 2, 0), (PieceEnum.s, 3, 0), (PieceEnum.d, 4, 0), (PieceEnum.p, 4, 1)]

    def __init__(self):
        self._board = self._initEmptyBoard()
        self._pieces = []

    #adds some pieces, takes None, returns None
    def addInitialPieces(self, initialPositions=None) -> None:

        if not initialPositions:
            for piece, dx, dy in Board.INITIAL_ARRANGEMENT:
                self._pieces.append(self._board[dx][Board.BOARD_SIZE-1-dy].addPiece(piece, PlayerEnum.UPPER))
                self._pieces.append(self._board[Board.BOARD_SIZE-dx-1][dy].addPiece(piece, PlayerEnum.LOWER))
        else:
            # here, the initial arrangements have been set by file
            for pieceInfo in initialPositions:
                pos, pieceVal = pieceInfo['position'], pieceInfo['piece']

                x,y = coordStringToCoord(pos)
                
                # we know this piece has been promoted initially
                promoted = len(pieceVal) == 2 and pieceVal[0] == '+'
                piece = PieceEnum[pieceVal[-1].lower()]
                player = PlayerEnum.UPPER if pieceVal[-1].isupper() else PlayerEnum.LOWER
                
                #subtract by one to account for 0 indexing
                self._pieces.append(self._board[x-1][y-1].addPiece(piece, player, promoted=promoted))

    # finds the location of the drive piece as a tuple
    def _driveLocation(self, playerType)->tuple:
        for p in self._playerPieces(playerType):
            if p._pieceType == PieceEnum.d:
                return p._coord, p

        print('Error in Finding drive location', self._pieces)
        exit(1)

    # given two coordinates, returns the path that the checker is checking on
    def _inBetweenPath(self, coordA, coordB):

        pathList = []

        # vertical path

        if coordA[0] != coordB[0] and coordA[1] != coordB[1]:
            uVector = [1,1]
        elif coordA[1] != coordB[1]:
            uVector = [0,1]
        elif coordA[0] != coordB[0]:
            uVector = [1,0]

        startCoord, endCoord = (coordA, coordB) if coordA[0] + coordA[1] < coordB[0] + coordB[1] else (coordB, coordA)

        # uses the delta vector to print some paths
        for delta in range(1, max(endCoord[0] - startCoord[0], endCoord[1] - startCoord[1])):
            dVector = [uVector[0] * delta, uVector[1] * delta]
            pathList.append((dVector[0] + startCoord[0], dVector[1] + startCoord[1]))
        
        return pathList

    # returns if piece can reach a certain coordinate
    def _pieceCanReach(self, piece, coord, ignoreSide=False):

        # print(piece, piece.getValidMoves(self._board))
        # print(list(filter(lambda x: x._playerType == PlayerEnum.UPPER, self._pieces)))

        for c in piece.getValidMoves(self._board, ignoreSide):

            if c[0] == coord[0] and c[1] == coord[1]:
                return True
        return False

    # given a playerType, returns all relevant pieces in a list
    def _playerPieces(self, playerType):
        return list(filter(lambda x: x._playerType == playerType and not x._captured, self._pieces))

    def _reachablePieces(self, playerType, coord, ignoreSide=False):
        pieces = []
        for p in self._playerPieces(playerType):
            if self._pieceCanReach(p, coord, ignoreSide):
                pieces.append(p)

        return pieces

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