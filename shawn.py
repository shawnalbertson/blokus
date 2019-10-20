import pygame

# Load images
try:
    green = pygame.image.load("green.png")
except:
    print("Cannot load image")
    raise SystemExit
try:
    red = pygame.image.load("red.png")
except:
    print("Cannot load image")
    raise SystemExit
try:
    yellow = pygame.image.load("yellow.png")
except:
    print("Cannot load image")
    raise SystemExit
try:
    blue = pygame.image.load("blue.png")
except:
    print("Cannot load image")
    raise SystemExit

try:
    white = pygame.image.load("white.png")
except:
    print("Cannot load image")
    raise SystemExit

# Change tile size to fit n per edge - a regular Blokus board is 20x20
# Do this by using modifier n on (x,y) tuple "size"
size = (700, 700)

n = 20
x_size = int(size[0]/n)
y_size = int(size[1]/n)

green = pygame.transform.scale(green, (x_size, y_size))
red = pygame.transform.scale(red, (x_size, y_size))
yellow = pygame.transform.scale(yellow, (x_size, y_size))
blue = pygame.transform.scale(blue, (x_size, y_size))
white = pygame.transform.scale(white, (x_size, y_size))
##MAKE PIECES



















# Initialize pygame visual display and other things??
pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Blockus')
background_color = (177,177,177)
screen.fill(background_color)

for m in range(20):
    for n in range(20):
        screen.blit(white, (x_size*m, y_size*n))
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


