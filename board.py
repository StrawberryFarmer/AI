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
        self.last_move = None

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

        def pawn_moves():
            if piece.moved: #important to check if the pawn has already moved because it influences how it is able to move
                steps = 1
            else:
                steps = 2

            #moving
            start = row + piece.direction
            end = row + (piece.direction * (1 + steps))
            for move_row in range(start, end, piece.direction): #loops the column which the pawn can move
                if Square.in_range(move_row):
                    if self.squares[move_row][col].is_empty(): #validates the vertical move
                        initial = Square(row, col)
                        final = Square(move_row, col)
                        #creating and adding the move into the list of available moves
                        move = Move(initial, final)
                        piece.add_move(move)
                    else: #if the pawn is blocked in front of it, do not display anything
                        break
                else:
                    break
            
            #capturing
            move_row = row + piece.direction
            move_cols = [col-1, col+1] #where capturing to the left or right
            for move_col in move_cols:
                if Square.in_range(move_row, move_col):
                    if self.squares[move_row][move_col].has_enemy_piece(piece.colour): #checks if there is a piece to capture in either diagonal
                        initial = Square(row, col)
                        final = Square(move_row, move_col)
                        #creating and adding the move into the list of available moves
                        move = Move(initial, final)
                        piece.add_move(move)

        def straight_line_moves(steps): #for the rook, bishop, and queen

            for step in steps:
                row_step, col_step = step
                move_row = row + row_step
                move_col = col + col_step

                while True:
                    if Square.in_range(move_row, move_col):

                        #creating a move
                        initial = Square(row, col)
                        final = Square(move_row, move_col)
                        move = Move(initial, final)

                        #when empty
                        if self.squares[move_row][move_col].is_empty():
                            piece.add_move(move)

                        #when enemy piece is there
                        if self.squares[move_row][move_col].has_enemy_piece(piece.colour):
                            piece.add_move(move)
                            break

                        #when allied piece is there
                        if self.squares[move_row][move_col].has_ally_piece(piece.colour):
                            break

                    else: #when no longer in range, either outside board or blocked by a piece
                        break
                            
                    #changing square    
                    move_row = move_row + row_step
                    move_col = move_col + col_step

        def king_moves():
            moves = [
                (row-1, col-1), #top left
                (row-1, col+0), #up
                (row-1, col+1), #top right
                (row+0, col+1), #right
                (row+1, col+1), #bottom right
                (row+1, col+0), #bottom
                (row+1, col-1), #bottom left
                (row+0, col-1), #left
            ]

            for move in moves:
                move_row, move_col = move

                #normal moves
                if Square.in_range(move_row, move_col):
                    if self.squares[move_row][move_col].is_empty_or_enemy(piece.colour):
                        initial = Square(row, col)
                        final = Square(move_row, move_col)
                        #creating and adding the move into the list of available moves
                        move = Move(initial, final)
                        piece.add_move(move)

                #castling moves
                if not piece.moved: #castling can only be done when the king hasn't moved yet

                    #King-side
                    right_rook = self.squares[row][7].piece
                    if isinstance(right_rook, Rook):
                        if not right_rook.moved: #the rook must also not have moved
                            for column in range(5, 7): #2 columns of space between the king and right rook
                                if self.squares[row][column].has_piece(): #goes through the columns in that row
                                    break #collision, there is at least one piece between rook and king
                                if column == 6: #castling is valid
                                    piece.right_rook = right_rook

                                    #creates and adds the king's move as valid to castle
                                    initial = Square(row, col)
                                    final = Square(row, 6)
                                    move = Move(initial, final)
                                    piece.add_move(move)

                                    #creates and adds the right rook's move as valid to castle
                                    initial = Square(row, 7)
                                    final = Square(row, 5)
                                    move = Move(initial, final)
                                    right_rook.add_move(move)

                    #Queen-side
                    left_rook = self.squares[row][0].piece
                    if isinstance(left_rook, Rook):
                        if not left_rook.moved: #the rook must also not have moved
                            for column in range(1, 4): #3 columns of space between the king and left rook
                                if self.squares[row][column].has_piece(): 
                                    break #collision, there is at least one piece between rook and king
                                if column == 3: #castling is valid
                                    piece.left_rook = left_rook

                                    #creates and adds the king's move as valid to castle
                                    initial = Square(row, col)
                                    final = Square(row, 2)
                                    move = Move(initial, final)
                                    piece.add_move(move)

                                    #creates and adds the left rook's move as valid to castle
                                    initial = Square(row, 0)
                                    final = Square(row, 3)
                                    move = Move(initial, final)
                                    left_rook.add_move(move)
                            

        if isinstance(piece, Pawn):
            pawn_moves()

        elif isinstance(piece, Bishop): #the tuple is in the form (row, col)
            straight_line_moves([
                (-1, -1), #towards top left
                (-1, 1), #towards top right
                (1, 1), #towards bottom right
                (1, -1) #towards bottom left
            ])
        
        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Rook):
            straight_line_moves([
                (0, 1), #horizontal right
                (0, -1), #horizontal left
                (-1, 0), #vertical up
                (1, 0) #vertical down
            ])

        elif isinstance(piece, King):
            king_moves()

        elif isinstance(piece, Queen):
            straight_line_moves([
                (-1, -1), #towards top left
                (-1, 1), #towards top right
                (1, 1), #towards bottom right
                (1, -1), #towards bottom left
                (0, 1), #horizontal right
                (0, -1), #horizontal left
                (-1, 0), #vertical up
                (1, 0) #vertical down
            ])

    def move(self, piece, move):
        initial = move.initial_square
        final = move.final_square

        #update the board array
        self.squares[initial.row][initial.col].piece = None #initial position will have no piece
        self.squares[final.row][final.col].piece = piece #final position will have the current piece

        #promotion
        if isinstance(piece, Pawn):
            self.check_promotion(piece, final)

        #castling
        if isinstance(piece, King):
            if self.castling(initial, final):
                difference = final.col - initial.col #determine which side the king has moved

                if difference < 0: #moves to the left
                    rook = piece.left_rook
                else: #moves to the right
                    rook = piece.right_rook

                self.move(rook, rook.moves[-1]) #uses the last added move in array, from the king_moves method

        piece.moved = True
        piece.moves = [] #valid moves are now different because the position of the piece is different, re-calculate

        #keep track of each move to display it
        self.last_move = move

    def valid_move_list(self, piece, move):
        return move in piece.moves

    def check_promotion(self, piece, final):
        if final.row == 0 or final.row == 7: #checks top and bottom rows, for white and black respectively
            self.squares[final.row][final.col].piece = Queen(piece.colour) #create a queen at this position

    def castling(self, initial, final):
        return abs(initial.col - final.col) == 2 #has the king moved 2 squares? only possible with castling
