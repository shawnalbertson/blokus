import pygame, sys
from pygame.locals import *

class Screen:
    def __init__(self, board_screen_dimension, fps):
        self.board_screen = board_screen_dimension
        self.fps = fps

    def start_board_display(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.board_screen, self.board_screen))

        # Avoid copyright issues with convenient typos
        pygame.display.set_caption('Blockus')
        self.screen.fill((177,177,177))
        self.clock = pygame.time.Clock()
    
    def display_update(self):
        pygame.display.update()
        self.clock.tick(self.fps)

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
        self.L5 = Piece(Screen, [["x", "x", "x"], ["x",".","."], ["x",".","."]], self.click_color)
        self.plus = Piece(Screen, [[".", "x", "."], ["x", "x", "x"], [".", "x", "."]], self.click_color)
        self.N = Piece(Screen, [[".", ".", "x", "x"], ["x", "x", "x", "."]], self.click_color)

class Tile:
    def __init__(self, Screen, tile_size, tile_x, tile_y):
        self.tile_size = tile_size
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.screen = Screen

        # set the tiles to grey initially
        self.color_code = "w"

        # define a rectangle
        self.rect = pygame.Rect(self.tile_x, self.tile_y, self.tile_size, self.tile_size)
        
        # # draw the rectangle
        
        # pygame.draw.rect(Screen.screen, (177,177,177), self.rect, 0)

        # load the image and then scale it
        im = pygame.image.load('white.png')
        self.image = pygame.transform.scale(im, (self.tile_size, self.tile_size))

    def check_mouse_over(self, mouse_x, mouse_y):
        if self.rect.collidepoint(mouse_x,mouse_y):
            return True
        else:
            return False
    
    def colors(self):
        if self.color_code == "w":
            self.image = pygame.transform.scale(pygame.image.load("white.png"), (self.tile_size, self.tile_size))
            return self.image
        elif self.color_code == "g":
            self.image = pygame.transform.scale(pygame.image.load("green.png"), (self.tile_size, self.tile_size))
            return self.image
        elif self.color_code == "r":
            self.image = pygame.transform.scale(pygame.image.load("red.png"), (self.tile_size, self.tile_size))
            return self.image
        elif self.color_code == "y":
            self.image = pygame.transform.scale(pygame.image.load("yellow.png"), (self.tile_size, self.tile_size))
            return self.image
        elif self.color_code == "b":
            self.image = pygame.transform.scale(pygame.image.load("blue.png"), (self.tile_size, self.tile_size))
            return self.image


    def draw_tile(self):
        self.screen.blit(self.colors(), (self.tile_x, self.tile_y))
        # print(self.colors(self.color_code))
    def assign_color_tile(self,Screen,Player):
        if self.color_code == 'w':
            self.color_code = Player.click_color
        else:
            self.color_code = self.color


class Board:
    def __init__(self, Screen):
        self.screen = Screen
        self.rows = 20
        self.columns = 20
        self.tile_size = int(self.screen.board_screen/self.rows)
        
        self.tiles = []
        # creating the tiles in a loop
        for row in range(0,self.rows):
            self.column = []
            for column in range(0,self.columns):
                self.tile = Tile(Screen, self.tile_size, row*self.tile_size, column*self.tile_size)
                self.column.append(self.tile)
                self.tile.draw_tile()
                
            self.tiles.append(self.column)

    def draw(self):
        for row, m in enumerate(self.tiles):
            for column, n in enumerate(m):
                n.draw_tile()  
    
    def modify_board(self, Piece, mouse_location):
        for row, m in enumerate(Piece):
            for column, n in enumerate(m):
                mouse_x = mouse_location[0]
                mouse_y = mouse_location[1]
                is_space_available = self.tiles[row + mouse_x][column + mouse_y].color_code
                if not n == "." and is_space_available == "w":
                    is_space_available = n
                elif not is_space_available == "w":
                    # change piece color to red version
                    pass
                else:
                    continue

class Piece(Board):

    def __init__(self, Screen, piece_array, color):
        super().__init__(Screen)
        self.piece_array = piece_array
        self.color = color
        self.screen = Screen
        for row, m in enumerate(self.piece_array):
            for column, n in enumerate(m):
                if not n == ".":
                    self.array[row][column] = self.color
                    
    def rotate_piece(self):
        """Modify array such that the piece rotates"""
        pass
    
    def draw(self):
        (start_x, start_y) = pygame.mouse.get_pos()

        for row, m in enumerate(self.tiles):
            for column, n in enumerate(m):
                n.draw_tile(self.screen)
