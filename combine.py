import pygame, sys
from pygame.locals import *

class Screen:
    def __init__(self, screen_width, screen_height, fps):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = fps

    def start_display(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Avoid copyright issues with convenient typos
        pygame.display.set_caption('Blockus')

        self.clock = pygame.time.Clock()
    
    def display_update(self):
        pygame.display.update()
        self.clock.tick(30)

class Player:
    def __init__(self, player_name, player_color):
        self.player_name = player_name
        self.player_color = player_color

        if self.player_color == "red":
            self.click_color = "r"
        if self.player_color == "blue":
            self.click_color = "b"
        if self.player_color == "green":
            self.click_color = "g"
        if self.player_color == "yellow":
            self.click_color = "y"
            
    def initialize_pieces(self, Screen):
        # create all of the pieces and assign a used or not used to them
        self.L5 = Piece(Screen, [["x", "x", "x"], ["x",".","."], ["x",".","."]])
        self.plus = Piece(Screen, [[".", "x", "."], ["x", "x", "x"], [".", "x", "."]])
        self.N = Piece(Screen, [[".", ".", "x", "x"], ["x", "x", "x", "."]])

class Tile:
    def __init__(self, Screen, tile_size, tile_x, tile_y):
        self.tile_size = tile_size
        self.tile_x = tile_x
        self.tile_y = tile_y

        # set the tiles to grey initially
        self.color_code = "w"

        # define a rectangle
        self.rect = pygame.Rect(self.tile_x, self.tile_y, self.tile_size, self.tile_size)
        
        # # draw the rectangle
        # pygame.draw.rect(Screen.screen, self.color, self.rect, 0)

        # load the image and then scale it
        im = pygame.image.load('white.png')
        self.image = pygame.transform.scale(im, (self.tile_size, self.tile_size))

    def check_mouse_over(self, mouse_x, mouse_y):
        if self.rect.collidepoint(mouse_x,mouse_y):
            return True
        else:
            return False
    
    def colors(self, color_code):
        if color_code == "w":
            self.image = pygame.transform.scale(pygame.image.load("white.png"), (self.tile_size, self.tile_size))
            return self.image
        elif color_code == "g":
            self.image = pygame.transform.scale(pygame.image.load("green.png"), (self.tile_size, self.tile_size))
            return self.image
        elif color_code == "r":
            self.image = pygame.transform.scale(pygame.image.load("red.png"), (self.tile_size, self.tile_size))
            return self.image
        elif color_code == "y":
            self.image = pygame.transform.scale(pygame.image.load("yellow.png"), (self.tile_size, self.tile_size))
            return self.image
        elif color_code == "b":
            self.image = pygame.transform.scale(pygame.image.load("blue.png"), (self.tile_size, self.tile_size))
            return self.image


    def draw_tile(self, Screen, Player):
        Screen.blit(colors(self.color_code), self.rect)
    
    def assign_color_tile(self,Screen,Player):
        if self.color == 'w':
            self.color = Player.click_color
        else:
            self.color = self.color


class Board:
    """ The object that contains all tile information

    Screen is a pygame surface object

    Tiles is an object with a few pre loaded tile images

    Array holds information about the colors of the board at the moment

    get_mouse determines if the image will follow your mouse or not
    """

    def __init__(self, screen, get_mouse = True):

        self.screen = screen
        self.size = tiles.size

        # Make color images
        self.white = tiles.tile1.image
        self.green = tiles.tile2.image
        self.red = tiles.tile3.image
        self.yellow = tiles.tile4.image
        self.blue = tiles.tile5.image

        self.array = array
        self.get_mouse = get_mouse

    def draw(self):
        """Draw a piece or a board to screen object
        Don't draw anything that's not w, g, r, y or b
        """
        if self.get_mouse:
            (start_x, start_y) = pygame.mouse.get_pos()
        else:
            (start_x, start_y) = (0,0)

        for i1, m in enumerate(self.array):
            for i2, n in enumerate(m):
                if n == "w":
                    self.screen.blit(self.white, (self.size*i1 + start_x, self.size*i2 + start_y))
                elif n == "g":
                    self.screen.blit(self.green, (self.size*i1 + start_x, self.size*i2 + start_y))
                elif n == "r":
                    self.screen.blit(self.red, (self.size*i1 + start_x, self.size*i2 + start_y))
                elif n == "y":
                    self.screen.blit(self.yellow, (self.size*i1 + start_x, self.size*i2 + start_y))
                elif n == "b":
                    self.screen.blit(self.blue, (self.size*i1 + start_x, self.size*i2 + start_y))                                                         
                else:
                    continue    
    
    def modify_board(self, modifier, start):
        """Rewrite certain chunks of array to a new color

        Used to change the big board over time

        modifier is another Board object that should relate to a piece
            contains colors
        
        start is a tuple relating to the current mouse location
            a.k.a where the piece is going to be dropped

        This is where snapping will come into play, because the mouse should get moved to a particular location for placing the piece

        This is a good place to check that the piece fits on the board in the first place
        """
        for i1, m in enumerate(modifier.array):
            for i2, n in enumerate(m):
                check = self.array[i1 + start[0]][i2 + start[1]]
                if not n == "." and check == "w":
                    self.array[i1 + start[0]][i2 + start[1]] = n
                elif not check == "w":
                    # raise NameError('No')
                else:
                    continue

class Piece(Board):

    def __init__(self, screen, tiles, array, get_mouse = True):
        super().__init__(screen, tiles, array, get_mouse)

    def rotate_piece(self):
        """Modify array such that the piece rotates"""
        pass

    def assign_color(self, Player):
        """Take in a general array representing a piece
        Assign the general fill with the newly definied fill
        """
        for i1, m in enumerate(self.array):
            for i2, n in enumerate(m):
                if not n == ".":
                    self.array[i1][i2] = Player.click_color
