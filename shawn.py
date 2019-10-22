import pygame
import time

from model import piece_size, Tile, Tiles, Board, Piece


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
def board_array():
    board = []
    row = []
    for m in range(20):
        for n in range(20):
            row.append("w")
        board.append(row)
        row = []
    return board

board_array = board_array()

# Create board object from board_array
b = Board(screen, tiles, board_array, False)

# Here are a few arrays that define pieces
L5_array = [["x", "x", "x"], ["x",".","."], ["x",".","."]]
plus_array = [[".", "x", "."], ["x", "x", "x"], [".", "x", "."]]
N_array = [[".", ".", "x", "x"], ["x", "x", "x", "."]]
blank_array = [["."]]

# Here we create Piece objects using these arrays
L5 = Piece(screen, tiles, L5_array)
plus = Piece(screen, tiles, plus_array)
N = Piece(screen, tiles, N_array)
blank = Piece(screen, tiles, blank_array)

# Assign colors to the pieces
L5.assign_color("r")
plus.assign_color("b")
N.assign_color("y")

def play_game(board, piece, draw = True):
    while draw:
        board.draw()
        piece.draw()
        for event in pygame.event.get():

            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = event.pos
                mouse_x = int(mouse_x/size)
                mouse_y = int(mouse_y/size)
                board.modify_board(piece, (mouse_x, mouse_y)) 
                draw = False
            pygame.display.flip()

            if event.type == pygame.QUIT:
                draw = False



play_game(b, L5)
play_game(b, blank)
play_game(b, plus)
play_game(b, blank)
play_game(b, N)
play_game(b, blank)
L5.assign_color("y")
play_game(b, L5)
play_game(b, blank)