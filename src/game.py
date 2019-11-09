from player import Player
from enum_values import *
from board import Board
from utils import *

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

    # starts the game
    def startGame(self):
        while self._num_turns <= 200 and self._gameState == GameState.PLAYING:
            print(self._board)
            
            commands = ['move e1 e4', 'move e5 e4', 'drop p c4']

            if self._num_turns >= len(commands) - 1:
                playerInput = input(f"{ self._currentPlayer._playerType.value}> ")
            else:
                playerInput = commands[self._num_turns]

            #parses the input
            self.parseInput(playerInput)

            #prints the captures -> Upper then Lower
            self._players[1].printCaptures()
            self._players[0].printCaptures()
        
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

            print((not fr.hasPiece()),(to._coord not in validMoves) ,(fr._piece._playerType != self._currentPlayer))
            exit(1)

        # we first remove our piece from our original destination
        fr.removePiece()

        if to.hasPiece():
            to.removePiece(drop=True, player=self._currentPlayer)

        to.placePiece(frPiece)

        print(f"{self._currentPlayer} player action: move {fr.name} {to.name}")
        
    def processDrop(self, pieceName: str, square):

        # ensure that drop zone is empty
        if square.hasPiece():
            self.endGame(EndGameType.INVALID_MOVE)
        
        dropPiece = self._currentPlayer.dropCapture(pieceName)
        
        if not dropPiece:
            print(dropPiece)
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

            self.processMove(frSquare, toSquare)

        elif inputSplit[0] == MoveType.DROP.value:

            dropCoord = coordStringToCoord(inputSplit[2])
            dropSquare = self._board._getBoard(*dropCoord)

            self.processDrop(inputSplit[1], dropSquare)

        else:
            print('Invalid Commond')
            

if __name__ == "__main__":
    game = Game()
    
    game.startGame()
    
