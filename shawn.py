import pygame

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


board_size = (700, 700)
size = piece_size(board_size, 20)

green = load_image("green.png", size)
red = load_image("red.png", size)
yellow = load_image("yellow.png", size)
blue = load_image("blue.png", size)
white = load_image("white.png", size)

# Change tile size to fit n per edge - a regular Blokus board is 20x20
# Do this by using modifier n on (x,y) tuple "size"
# size = (700, 700)

# n = 20
# x_size = int(size[0]/n)
# y_size = int(size[1]/n)

# green = pygame.transform.scale(green, (x_size, y_size))
# red = pygame.transform.scale(red, (x_size, y_size))
# yellow = pygame.transform.scale(yellow, (x_size, y_size))
# blue = pygame.transform.scale(blue, (x_size, y_size))
# white = pygame.transform.scale(white, (x_size, y_size))
##MAKE PIECES



















# Initialize pygame visual display and other things??
pygame.init()

screen = pygame.display.set_mode(board_size)
pygame.display.set_caption('Blockus')
background_color = (177,177,177)
screen.fill(background_color)

for m in range(20):
    for n in range(20):
        screen.blit(white, (size*m, size*n))


# These few lines place an L5 piece in the top left corner
# Next steps: how to generalize
#   make the blitting steps for every piece


(start_x, start_y) = pygame.mouse.get_pos()

print(start_x, start_y)

# start_x_tile = 7
# start_y_tile = 5

# start_x = x_size * start_x_tile
# start_y = y_size * start_y_tile

pos0 = -1
pos1 = 1

for m in [pos0 * i for i in range(3)]:
    screen.blit(blue, (size*m + start_x, 0 + start_y))

for m in [pos1 * i for i in range(3)]:
    screen.blit(blue, (0 + start_x, size*m + start_y))

pygame.display.update()
    
# screen.blit(green, (0,0))
# screen.blit(red, (x_size, y_size))
# screen.blit(yellow, (x_size*2, y_size*2))
# screen.blit(blue, (x_size*3, y_size*3))

pygame.display.flip()


running = True
while running:









    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


