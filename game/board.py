import pygame
import pygame_widgets
from pygame_widgets.button import Button
import time
import pandas as pd

class Board:
    
    def __init__(self, screen, width, height):
        self.board_pieces = pd.DataFrame(columns=['Image', 'Location', 'Piece Type'])
        self.board_pieces.set_index('Image')
        self.get_images()
        self.screen = screen
        self.create_board(width/4, 0)
    
    def get_images(self):
        self.settlement = pygame.image.load('venv/Images/Board Peices/settlement.png')
        self.settlement = pygame.transform.scale(self.settlement, (25, 25))
        self.wood = pygame.image.load('venv/Images/Board Peices/wood.png')
        self.wood = pygame.transform.scale(self.wood, (100, 100))
    
    def update_board(self):
        for index, piece in self.board_pieces.iterrows():
            self.screen.blit(piece['Image'], piece['Location'])
    
    def create_board(self, x, y):
        for i in range(3,6):
            y += 70
            for j in range(i):
                x += 90
                rect = self.wood.get_rect()
                rect.center = (x,y)
                self.board_pieces.loc[len(self.board_pieces)] = [self.wood, rect, 'tile']
            x -= (90 * i+1) + 45
        x += 90
        for i in range(4,2,-1):
            y += 70
            for j in range(i):
                x += 90
                rect = self.wood.get_rect()
                rect.center = (x,y)
                self.board_pieces.loc[len(self.board_pieces)] = [self.wood, rect, 'tile']
            x -= (90 * i+1) - 45
    
    def board_clicked(self, rect):
        self.board_pieces.loc[len(self.board_pieces)] = [self.settlement, rect, 'settlement']
        # self.screen.blit(self.settlement, (130, 160))
        print(rect.x)
        print(rect.y)