#importing needed libraries and files
import pygame
from constant_values import *
from board import Board
from drag import Drag

class Chess():
    def __init__(self):
        self.board = Board()
        self.drag = Drag()
        self.current_turn = "white"

    def show_background(self, surface):
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0: #checks each square that is even in each row or column
                    colour = pygame.Color("#eaebc8") #hexadecimal for a dim white
                else:
                    colour = pygame.Color("#1d7539") #hexadecimal for dark green

                #create the sprite for each square on the board
                rect = (col * sq_size, row * sq_size, sq_size, sq_size)
                pygame.draw.rect(surface, colour, rect)

    def show_pieces(self, surface):
        #loop through each square
        for row in range(rows):
            for col in range(cols):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece #get the instance of the piece at this square

                    if piece is not self.drag.piece:
                        piece.set_skin()
                        image = pygame.image.load(piece.skin) #get the image for this piece from the images folder
                        resolution = (col * sq_size + sq_size // 2, row * sq_size + sq_size // 2) 
                        image_center = resolution #centers the image
                        piece.skin_rect = image.get_rect(center=image_center) #puts the image into a pygame rectangle
                        surface.blit(image, piece.skin_rect) #displays the pygame rectangle with the image

    def show_moves(self, surface):
        if self.drag.dragging:
            piece = self.drag.piece

            for move in piece.moves: #loop all valid moves in array
                if (move.final_square.row + move.final_square.col) % 2 == 0:
                    colour = "#C86464"
                else:
                    colour = "#C84646"

                rect = (move.final_square.col * sq_size, move.final_square.row * sq_size, sq_size, sq_size)

                pygame.draw.rect(surface, colour, rect)

    def show_last_move(self, surface):
        if self.board.last_move:
            initial = self.board.last_move.initial_square
            final = self.board.last_move.final_square

            for pos in [initial, final]:
                if (pos.row + pos.col) % 2 == 0:
                    colour = pygame.Color("#FBFF47") #light yellow
                else:
                    colour = pygame.Color("#E0DE00") #dark yellow

                rect = (pos.col * sq_size, pos.row * sq_size, sq_size, sq_size)
                pygame.draw.rect(surface, colour, rect)


    def next_turn(self):
        if self.current_turn == "black":
            self.current_turn = "white"
        else:
            self.current_turn = "black"