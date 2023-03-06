class Move():
    def __init__(self, initial, final):
        self.initial_square = initial
        self.final_square = final

    def __eq__(self, other): #validating move based on position on the board
        return self.initial_square == other.initial_square and self.final_square == other.final_square
        