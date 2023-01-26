#importing needed libraries and files
from constant_values import *
import pygame

class Drag():
    def __init__(self):
        self.m_posX = 0 #x-coordinate of mouse
        self.m_posY = 0 #y-coordinate of mouse
        self.initial_row = 0 #the row where the mouse is
        self.initial_col = 0 #the column where the mouse is
        self.piece = None #the current piece
        self.dragging = False #if a piece is being dragged (holding down of left click)

    def update_mouse(self, pos):
        self.m_posX, self.m_posY = pos #pos will be a tuple with (x,y) co-ordinates

    def save_initial_pos(self, pos):
        self.initial_row = pos[1] // sq_size #rows correspond to the y co-ordinate
        self.initial_col = pos[0] // sq_size #column correspond to the x co-ordinate

    def drag_piece(self, piece):
        self.piece = piece #stores the data of the piece currently dragged
        self.dragging = True #allows for logic in the main loop
    
    def undrag_piece(self):
        self.piece = None #removes the data of the piece currently dragged
        self.dragging = False #exits the if statement in the main game loop

    def update_blit(self, surface):
        self.piece.set_skin(size=128) #gets the image for a larger version of the current piece
        skin = self.piece.skin

        image = pygame.image.load(skin) #load the image so it can be used in a rectangle
        image_center = (self.m_posX, self.m_posY)
        self.piece.skin_rect = image.get_rect(center=image_center) #centers the image on the cursor

        surface.blit(image, self.piece.skin_rect) #blits the image onto the screen
