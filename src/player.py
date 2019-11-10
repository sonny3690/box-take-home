from enum_values import *

class Player:
    
    def __init__(self, playerType):
        self._playerType = playerType
        self._captures = []

    # player type is upper
    def _isUpper(self):
        return self._playerType == PlayerEnum.UPPER

    def addCapture(self, piece):
        self._captures.append(piece)

    # prints all the captures
    def printCaptures(self):
        captureString = ' '.join(list(map(str, self._captures)))
        return f"Captures {self._playerType.value}: {captureString}"

    def dropCapture(self, pieceName: str):    
        # go through all the captures
        for i, c in enumerate(self._captures):

            if str(c).lower() == pieceName:
                # returns the piece object to drop
                return self._captures.pop(i)
        return None      

    def __str__(self):
        return self._playerType.value