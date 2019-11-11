

def parseTestCase(path):
    """
    Utility function to help parse test cases.
    :param path: Path to test case file.
    """
    f = open(path)
    line = f.readline()
    initialBoardState = []
    while line != '\n':
        piece, position = line.strip().split(' ')
        initialBoardState.append(dict(piece=piece, position=position))
        line = f.readline()
    line = f.readline().strip()
    upperCaptures = [x for x in line[1:-1].split(' ') if x != '']
    line = f.readline().strip()
    lowerCaptures = [x for x in line[1:-1].split(' ') if x != '']
    line = f.readline()
    line = f.readline()
    moves = []
    while line != '':
        moves.append(line.strip())
        line = f.readline()

    return dict(initialPieces=initialBoardState, upperCaptures=upperCaptures, lowerCaptures=lowerCaptures, moves=moves)

# just converts a column number to a column character
def convertColNumToChar(colNum: int) -> str:
    return chr(ord('a') + colNum - 1)

# does the opposite as convertColNumToChar except with reverse mapping
def convertColCharToNum(colChar: str) -> int:
    return ord(colChar) - ord('a') + 1

# given x and y, returns if off coordinate
def oob(x: int, y: int, boardSize=5)-> bool:
    return x <= 0 or x > boardSize or y <=0 or y > boardSize

# coord string to coord
# returns None if invalid
def coordStringToCoord(s: str) -> tuple:

    assert(len(s) == 2)

    return convertColCharToNum(s[0]), int(s[1])

# return coord to string
def coordToString(t: tuple):
    return convertColNumToChar(t[0]) + str(t[1])

# returns if the same coordinate
def sameCoord(t1: tuple, t2: tuple) -> bool:
    return t1[0] == t2[0] and t1[1] == t2[1]

    

    


