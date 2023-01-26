#importing needed libraries and files
from constant_values import *
from piece import *
from square import Square
from move import Move

class Board():
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]] #a visual representation of the board

        self.create_board()
        self.add_piece_to_square(chosen_colour)
        self.add_piece_to_square(not_chosen_colour)

    def create_board(self):
        #looping through each square
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row, col) #creating an instance of square at each position in the array

    def add_piece_to_square(self, colour):
        if colour == chosen_colour: #the player's starting rows (at the bottom)
            row_pawn = 6
            row_other = 7
        else: #the AI's starting rows (at the top)
            row_pawn = 1
            row_other = 0
        
        for col in range(cols):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(colour)) #creates a row of pawns

        #creating knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(colour)) #knight on the left side
        self.squares[row_other][6] = Square(row_other, 6, Knight(colour)) #knight on the right side

        self.squares[4][4] = Square(4, 4, Knight(colour))

        #creating bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(colour)) #bishop on the left side
        self.squares[row_other][5] = Square(row_other, 5, Bishop(colour)) #bishop on the right side

        #creating rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(colour)) #rook on the left side
        self.squares[row_other][7] = Square(row_other, 7, Rook(colour)) #rook on the right side

        #creating queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(colour))

        #creating king
        self.squares[row_other][4] = Square(row_other, 4, King(colour))

    def valid_moves(self, piece, row, col):

        def knight_moves():
            # has a maximum of 8 possible moves
            possible_moves = [
                (row-2, col+1), #top right
                (row-1, col+2), #top right
                (row+1, col+2), #bottom right
                (row+2, col+1), #bottom right
                (row+2, col-1), #bottom left
                (row+1, col-2), #bottom left
                (row-1, col-2), #top left
                (row-2, col-1), #top left
            ]
            
            for possible_move in possible_moves: #loop through all possible moves
                possible_move_row, possible_move_col = possible_move #split into row and column like in the tuple

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].is_empty_or_enemy(piece.colour): #the move is valid if the square is empty or there is an enemy piece there
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) #need to send a piece later

                        move = Move(initial, final) #parse the starting and ending square of the move
                        piece.add_move(move) #add to the array of valid moves
        
        if isinstance(piece, Pawn):
            pass

        elif isinstance(piece, Bishop):
            pass
        
        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Rook):
            pass

        elif isinstance(piece, King):
            pass

        elif isinstance(piece, Queen):
            pass