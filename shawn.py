import pygame
import time


# Initialize pygame, screen object
pygame.init()

board_size = (700, 700)
screen = pygame.display.set_mode(board_size)

# Avoid copyright issues with convenient typos
pygame.display.set_caption('Blockus')

# This gray color fill is meaningless once pieces start getting placed
background_color = (177,177,177)
screen.fill(background_color)

# Load images

def piece_size(board_size, n):
    """Take board dimension tuple and number of desired pieces per board
    Return the length of one edge of a tile as int type for pygame.transform.scale

    A regular Blokus board is 20x20
    """
    return int(min(board_size)/n)

def load_image(file_name, size):
    """ Take file as filename
    Take board size as length 2 tuple
    Scale each image such that it fits as a square
    """
    try:
        im = pygame.image.load(file_name)

    except:
        print("Cannot load image")
        raise SystemExit

    return pygame.transform.scale(im, (size, size))

# Define the size of one tile
size = piece_size(board_size, 20)

# Load predrawn tiles and give them names that match
green = load_image("green.png", size)
red = load_image("red.png", size)
yellow = load_image("yellow.png", size)
blue = load_image("blue.png", size)
white = load_image("white.png", size)

# Function to draw a board with white tile pieces to start
def draw_board():
    for m in range(20):
        for n in range(20):
            screen.blit(white, (size*m, size*n))

# These few lines place an L5 piece in the top left corner
# Next steps: more general
#   make the blitting steps for every piece


def L5(color, mod0, mod1):
    """the mod inputs allow rotation, should be +/- 1"""
    (start_x, start_y) = pygame.mouse.get_pos()

    for m in [mod0 * i for i in range(3)]:
        screen.blit(color, (size*m + start_x, 0 + start_y))

    for m in [mod1 * i for i in range(3)]:
        screen.blit(color, (0 + start_x, size*m + start_y))


# Stop the code when the window is closed
running = True
while running:
    draw_board()
    L5(red, 1, 1)
    time.sleep(.01)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

