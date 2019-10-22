import pygame
import time

from model import piece_size, Tile, Tiles, Board, Piece
from controller import board_array



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


# Make the necessary Tile objects
white = Tile("white.png", size, ".")
green = Tile("green.png", size, "g")
red = Tile("red.png", size, "r")
yellow = Tile("yellow.png", size, "y")
blue = Tile("blue.png", size, "b")

# Add them to a Tiles object to be concise
tiles = Tiles(white, green, red, yellow, blue)

# Call board_array() to make the base board
board_array = board_array()

# Create board object from board_array
b = Board(screen, tiles, board_array, False)

# Here are a few arrays that define pieces
L5_array = [["x", "x", "x"], ["x",".","."], ["x",".","."]]
plus_array = [[".", "x", "."], ["x", "x", "x"], [".", "x", "."]]
N_array = [[".", ".", "x", "x"], ["x", "x", "x", "."]]

# Here we create Piece objects using these arrays
L5 = Piece(screen, tiles, L5_array)
plus = Piece(screen, tiles, plus_array)
N = Piece(screen, tiles, N_array)

# Assign colors to the pieces
L5.assign_color("r")
plus.assign_color("b")
N.assign_color("y")

# Visualize it
running = True
while running:
    b.draw()
    # L5.draw()
    # plus.draw()
    N.draw()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
