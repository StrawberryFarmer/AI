#importing main libraries and classes from other files
import pygame
import sys
from constant_values import *
from chess import Chess

class Main():
    def __init__(self): #initialise the main game window
        pygame.init()
        self.screen = pygame.display.set_mode((width, height)) #creates the screen using width and height variables in a tuple as the size
        pygame.display.set_caption("Chess AI") #creates the title of the game window
        self.chess = Chess()

    def game_loop(self): #responsible for running the game
        screen = self.screen
        chess = self.chess
        drag = self.chess.drag
        board = self.chess.board

        while True:
            self.chess.show_background(screen) #displays the background squares and their colours
            self.chess.show_moves(screen) #displays possible moves
            self.chess.show_pieces(screen) #displays the pieces on the board


            if drag.dragging:
                drag.update_blit(screen)

            for event in pygame.event.get(): #checks through all pygame events each loop

                if event.type == pygame.MOUSEBUTTONDOWN: #click
                    drag.update_mouse(event.pos)
                    clicked_row = drag.m_posY // sq_size #gets the row of the position
                    clicked_col = drag.m_posX // sq_size #gets the col of the postiion

                    if board.squares[clicked_row][clicked_col].has_piece(): #check if the position clicked contains a piece
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.valid_moves(piece, clicked_row, clicked_col) #gets the valid moves of the piece at this square
                        drag.save_initial_pos(event.pos) #save the row and column of this piece
                        drag.drag_piece(piece) #changes attribute to allow moving the piece
                        
                        #displays as per the beginning of the game loop, but with updated information
                        chess.show_background(screen)
                        chess.show_moves(screen)
                        chess.show_pieces(screen)

                elif event.type == pygame.MOUSEMOTION: #mouse movement after click
                    if drag.dragging:
                        drag.update_mouse(event.pos) #updates the position of mouse
                        chess.show_background(screen) #draws the squares in the background again
                        chess.show_moves(screen) #draws the moves of the piece again
                        chess.show_pieces(screen) #draws the pieces on the board again
                        drag.update_blit(screen) #updates the image of the piece being dragged based on the position of mouse

                elif event.type == pygame.MOUSEBUTTONUP: #release
                    drag.undrag_piece()

                elif event.type == pygame.QUIT: #checks if the user exited the program
                    pygame.quit() #uninitialise pygame
                    sys.exit() #close the window

            pygame.display.update() #updates the screen to show any changes


main = Main()
main.game_loop()