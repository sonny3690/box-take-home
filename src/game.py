from player import Player
from enum_values import *
from board import Board
from utils import *
from piece import Piece
import sys


class Game:
    def __init__(self):
        self._num_turns = 0
        self._gameState = GameState.PLAYING
        self._players = [Player(PlayerEnum.LOWER), Player(PlayerEnum.UPPER)]
        self._board = Board()

    @property
    def _boardSquares(self):
        return self._board._board

    @property
    def _currentPlayer(self):
        return self._players[self._num_turns % 2]
    
    @property
    def _otherPlayer(self):
        return self._players[(self._num_turns+1) % 2]

    def initGame(self, fileInfo):
        if fileInfo == None:
            self._board.addInitialPieces()
        else:
            self._board.addInitialPieces(fileInfo['initialPieces'])
            
            for pieceVal in fileInfo['upperCaptures']:
                self._players[1].addCapture(Piece(PieceEnum[pieceVal.lower()], 0, 0, PlayerEnum.UPPER))

            for pieceVal in fileInfo['lowerCaptures']:
                self._players[0].addCapture(Piece(PieceEnum[pieceVal.lower()], 0, 0, PlayerEnum.LOWER))


    # starts the game
    def startGame(self, fileInfo):
        
        fileMode = fileInfo != None

        # print(fileInfo)
        
        while self._num_turns < 200 and self._gameState == GameState.PLAYING:

            '''
            Says should print certain information about the game state

            '''
            shouldPrint = not fileMode or (self._num_turns == len(fileInfo['moves'])-1)
            commands = fileInfo['moves'] if fileMode else []

            if self._num_turns >= len(commands):
                playerInput = input(f"{ self._currentPlayer._playerType.value}> ")
            else:
                playerInput = commands[self._num_turns]

            if shouldPrint:
                print(f"{self._currentPlayer} action: {playerInput}")
                print(self._board)


            #parses the input
            self.parseInput(playerInput)

            #prints the captures -> Upper then Lower
            if shouldPrint:
                self._players[1].printCaptures()
                self._players[0].printCaptures()
                print()
        
            # Do some stuff here
            self._num_turns += 1
            

        print('Tie game. Too many moves.')
    
    # Ends the game and exits the REPL
    def endGame(self, endGameType):
        
        print(f"{str(self._otherPlayer)} wins. {endGameType.value}")
        exit(0)
        
    # processes a move based on squares
    def processMove(self, fr, to, promote=False):
        frPiece = fr._piece
        
        validMoves = frPiece.getValidMoves(self._boardSquares)
        
        '''
        Covers the following cases that are invalid
        1) If fr square is empty
        2) If move is invalid
        3) If selected piece is opponent's piece
        '''
        if (not fr.hasPiece()) or (to._coord not in validMoves) or (fr._piece._playerType != self._currentPlayer._playerType):
            # small problem here; we're trying to move into each other
            self.endGame(EndGameType.INVALID_MOVE)
        

        # we first remove our piece from our original destination
        fr.removePiece()

        if to.hasPiece():
            to.removePiece(drop=True, player=self._currentPlayer)

        to.placePiece(frPiece)

        # print(f"{self._currentPlayer} player action: move {fr.name} {to.name}")

        '''
        Covers the following cases
        1) When a pawn reaches its promotion zone
        2) When user flags for a promotion
        '''
        if (frPiece._pieceType == PieceEnum.p and to.inPromotionZone()) or promote:
            
            '''
            Means that the game will end for the follopwing cases
            1) outside the promotion zone
            2) box drive or a shield is asked to be promoted
            '''
            if not (fr.inPromotionZone(self._currentPlayer) or to.inPromotionZone()) or (frPiece._pieceType == PieceEnum.d or frPiece._pieceType == PieceEnum.s):
                self.endGame(EndGameType.INVALID_MOVE)
        
            frPiece.promotePiece()
                        
    def processDrop(self, pieceName: str, square):
        # ensure that drop zone is empty
        if square.hasPiece():
            self.endGame(EndGameType.INVALID_MOVE)
        
        dropPiece = self._currentPlayer.dropCapture(pieceName)

        pDrop = True

        if pieceName == PieceEnum.p.value:

            x = square._x -1
            
            for y in range(Board.BOARD_SIZE):
                cSquare = self._boardSquares[x][y]
                
                '''
                Checks for Three Things
                1. If Square has a piece
                2. If square contains piece of p Type
                3. If square shares same player type
                '''

                if cSquare.hasPiece() and cSquare._piece._pieceType == PieceEnum.p and cSquare._playerType == self._currentPlayer._playerType:
                    pDrop = False

            # case in which p is dropped into promotion zone
            if square.inPromotionZone(self._currentPlayer):
                pDrop = False

        if not dropPiece or not pDrop:
            self.endGame(EndGameType.INVALID_MOVE)

        square.placePiece(dropPiece)
        
    # parses the input
    def parseInput(self, playerInput: str):
        promoted = False
        inputSplit = playerInput.split()

        assert(len(inputSplit) <= 4)

        if len(inputSplit) == 4:
            assert(inputSplit[-1] == 'PROMOTED' and inputSplit[0] == MoveType.MOVE.value)
            promoted = True
            inputSplit = inputSplit[:4]

        # ensure that there are three commands
        assert(len(inputSplit) == 3 and inputSplit[1] != inputSplit[2])

        if inputSplit[0] == MoveType.MOVE.value:

            # from and to coordinates
            fr, to = inputSplit[1:]
            frCoord, toCoord = coordStringToCoord(fr), coordStringToCoord(to)
            #Square
            frSquare, toSquare = self._board._getBoard(*frCoord), self._board._getBoard(*toCoord)

            if not frSquare.hasPiece():
                self.endGame(EndGameType.INVALID_MOVE)               

            self.processMove(frSquare, toSquare, promoted)

        elif inputSplit[0] == MoveType.DROP.value:

            dropCoord = coordStringToCoord(inputSplit[2])
            dropSquare = self._board._getBoard(*dropCoord)

            self.processDrop(inputSplit[1], dropSquare)

        else:
            print('Invalid Commond')


if __name__ == "__main__":
    game = Game()
    
    if not (len(sys.argv) == 2 and sys.argv[1] == '-i') and not (len(sys.argv) == 3 and sys.argv[1] == '-f'):
        print('Please format your argument as: python3 game.py [-i | -f]')
        exit(1)

    fileInfo = None

    if sys.argv[1] == '-f':
        fileInfo = parseTestCase(sys.argv[2])

    game.initGame(fileInfo)
    game.startGame(fileInfo)
    
