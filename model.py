import pygame

# Functions to load images
def piece_size(board_size, n):
    """Take board dimension tuple and number of desired pieces per board
    Return the length of one edge of a tile as int type for pygame.transform.scale

    A regular Blokus board is 20x20
    """
    return int(min(board_size)/n)

class Tile:
    """Includes color and size of tiles
    Reads image_file and makes it a scaled surface object
    Takes size found in main script
    Takes color_code for referring to different kinds of tiles
    """

    def __init__(self, image_file, size, color_code):
        im = pygame.image.load(image_file)
        self.image = pygame.transform.scale(im, (size, size))
        self.size = size
        self.color_code = color_code

class Tiles:
    """A more convenient way to store multiple tile objects that share information
    pass in order white, green, red, yellow, blue
    """
    def __init__(self, tile1, tile2, tile3, tile4, tile5):
        self.tile1 = tile1
        self.tile2 = tile2
        self.tile3 = tile3
        self.tile4 = tile4
        self.tile5 = tile5
        self.size = tile1.size

class Board:
    """ The object that contains all tile information

    Screen is a pygame surface object

    Tiles is an object with a few pre loaded tile images

    Array holds information about the colors of the board at the moment

    get_mouse determines if the image will follow your mouse or not
    """

    def __init__(self, screen, tiles, array, get_mouse = True):

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
        pass

class Piece(Board):

    def __init__(self, screen, tiles, array, get_mouse = True):
        super().__init__(screen, tiles, array, get_mouse)

    def rotate_piece(self):
        """Modify array such that the piece rotates"""
        pass

    def assign_color(self, color):
        """Take in a general array representing a piece
        Assign the general fill with the newly definied fill
        """
        for i1, m in enumerate(self.array):
            for i2, n in enumerate(m):
                if n == "x":
                    self.array[i1][i2] = color
