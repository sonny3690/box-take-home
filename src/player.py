from enum_values import *

class Player:
    
    def __init__(self, playerType):
        self._playerType = playerType
        self._droppedPieces = []

    # player type is upper
    def _isUpper(self):
        return self._playerType == PlayerEnum.UPPER

    def addDroppedPiece(self, piece):
        self._droppedPieces.append(piece)


    def __str__(self):
        return self._playerType.value


    
        
    

    
        