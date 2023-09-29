import pygame
import pygame_widgets
from pygame_widgets.button import Button
import time
from board import Board

width = 800
height = 600
click = False

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((width, height))

#Title and Icon
pygame.display.set_caption("Catan")
# icon = pygame.image.load()
# pygame.display.set_icon(icon)

# button = Button(
#     screen, 100, 100, 300, 150, text="hello",
#     fontsize=50, margin=20,
#     inactiveColour=(255,0,0),
#     pressedColour=(0,255,0), radius=20,
#     onClick=lambda: print('Click')
# )

# Create Board Object
board = Board(screen, width, height)

#Game Loop
running = True
while(running):
    # RGB        
    screen.fill((255,255,255))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            for rect in board.board_pieces.loc[board.board_pieces['Piece Type'] == 'tile']['Location']:
                if rect.collidepoint(event.pos):
                    if click:
                        board.board_clicked(rect)
                        click = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         changeX = -0.1
    
    board.update_board()
    
    pygame_widgets.update(events)
    pygame.display.update()
    