import pygame
import time

from model import Board, Piece, piece_size, load_image



# Initialize pygame, screen object
pygame.init()

board_size = (700, 700)
screen = pygame.display.set_mode(board_size)

# Avoid copyright issues with convenient typos
pygame.display.set_caption('Blockus')

# This gray color fill is meaningless once pieces start getting placed
background_color = (177,177,177)
screen.fill(background_color)

# Define the size of one tile
size = piece_size(board_size, 20)

# Load predrawn tiles and give them names that match
green = load_image("green.png", size)
red = load_image("red.png", size)
yellow = load_image("yellow.png", size)
blue = load_image("blue.png", size)
white = load_image("white.png", size)


b = Board(screen, size, white, green, red, yellow, blue)

# These few lines place an L5 piece in the top left corner
# Next steps: more general
#   make the blitting steps for every piece

L5 = Piece(screen, size, red, [["x", "x", "x", ".", "."], ["x",".",".",".","."], ["x",".",".",".","."]])


# Stop the code when the window is closed
running = True
while running:
    b.make_board()
    # L5(red, 1, 1)
    L5.draw_piece()
    time.sleep(.01)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

