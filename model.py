# Function to draw a board with white tile pieces to start
import pygame

# Functions to load images
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
    # try:
    #     im = pygame.image.load(file_name)

    # except:
    #     print("Cannot load image")
    #     raise SystemExit
    im = pygame.image.load(file_name)

    return pygame.transform.scale(im, (size, size))

class Board:
    """ The object that contains all tile information

    base, c1, c2, c3, c4 are all tile images
    """
    def __init__(self, screen, size, base, c1, c2, c3, c4):
        self.board = []
        self.row = []
        for m in range(20):
            for n in range(20):
                self.row.append(".")
            self.board.append(self.row)
            self.row = []

        self.screen = screen
        self.size = size
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4        
            
    def make_board(self):
        """Define board for optional input conditions. 
        All periods means a base board

        base tile = "."
        green tile = "g"
        red tile = "r"
        yellow tile = "y"        
        blue tile = "b"

        """        
        for i1, m in enumerate(self.board):
            for i2, n in enumerate(m):
                if n == ".":
                    self.screen.blit(self.base, (self.size*i1, self.size*i2))
                elif n == "g":
                    self.screen.blit(self.c1, (self.size*i1, self.size*i2))
                elif n == "r":
                    self.screen.blit(self.c2, (self.size*i1, self.size*i2))
                elif n == "y":
                    self.screen.blit(self.c3, (self.size*i1, self.size*i2))
                elif n == "b":
                    self.screen.blit(self.c2, (self.size*i1, self.size*i2))


class Piece:
    """There will be an instance for every piece
    Draw the shape in a 3x5 list of characters

    the L5 piece might be:
    [["x", "x", "x", ".", "."], ["x",".",".",".","."], ["x",".",".",".","."]]
    """

    def __init__(self, screen, size, color, array):
        self.screen = screen
        self.size = size
        self.color = color       
        self.array = array
    
  
    def draw_piece(self):
        (start_x, start_y) = pygame.mouse.get_pos()
        for i1, m in enumerate(self.array):
            for i2, n in enumerate(m):
                if n == "x":
                    self.screen.blit(self.color, (self.size*i1 + start_x, self.size*i2 + start_y))
                else:
                    continue
