#importing needed libraries and files
from constant_values import *
import os

class Piece():
    def __init__(self, name, colour, value, skin=None, skin_rect=None):
        self.name = name
        self.colour = colour
        if colour == chosen_colour: #change value of pieces for AI
            value_mult = 1 #allied pieces will have positive values
        else:
            value_mult = -1 #enemy pieces will have negative values
        self.value = value * value_mult
        self.skin = skin
        self.set_skin()
        self.skin_rect = skin_rect
        self.moves = []
        self.moved = False
    
    def set_skin(self, size=80):
        self.skin = os.path.join(f"code/images/imgs-{size}px/{self.colour}_{self.name}.png") #builds an f string to match name of image in images folder

    def add_move(self, move):
        self.moves.append(move) #add available moves into an array for move validation

class Pawn(Piece):
    def __init__(self, colour):
        if colour == "white": #used to identify whether the pawn should move up or down
            self.direction = 1
        else: #FIX DIRECTION
            self.direction = -1
        
        super().__init__("pawn", colour, 1) # initialises the attributes from the inherited class

class Knight(Piece):
    def __init__(self, colour):
        super().__init__("knight", colour, 3)

class Bishop(Piece):
    def __init__(self, colour):
        super().__init__("bishop", colour, 3)

class Rook(Piece):
    def __init__(self, colour):
        super().__init__("rook", colour, 5)

class Queen(Piece):
    def __init__(self, colour):
        super().__init__("queen", colour, 9)

class King(Piece):
    def __init__(self, colour):
        super().__init__("king", colour, 9999)