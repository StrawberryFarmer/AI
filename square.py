class Square():
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece != None #return the piece if the square has one

    def has_enemy_piece(self, colour):
        return self.has_piece() and self.piece.colour != colour #checks if there is a piece and if it is a different colour

    def has_ally_piece(self, colour):
        return self.has_piece() and self.piece.colour == colour #checks if there is a piece and if it is the same colour

    def is_empty(self):
        return not self.has_piece() #if the square does not have a piece, it must be empty

    def is_empty_or_enemy(self, colour):
        return self.is_empty() or self.has_enemy_piece(colour) #returns true if either method returns true

    @staticmethod #can be called without creating an instance of the class, and not specific to an instance
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7: #checks if the row or column is outside the board
                return False
        return True