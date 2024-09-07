class piece:
    x = 0
    y = 0
    location = [x,y]

    def __init__(self,x,y):
        self.x = x
        self.y = y

class Bishop:

    moveset = [
        8, 0, 8,
        0, 0, 0,
        8, 0, 8
    ]

    def __init__(self,x,y):
        super(piece(x,y))

class Rook:

    moveset = [
        0, 8, 0,
        8, 0, 8,
        0, 8, 0
    ]

class Pawn:

    moveset = [
        1, [1,2], 1,
        0, 0, 0,
        0, 0, 0
    ]

    movedAlready = False

class