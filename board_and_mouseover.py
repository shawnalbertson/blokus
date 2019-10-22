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

class Tile:
    def __init__(self, Screen, tile_width, tile_height, tile_x, tile_y):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_x = tile_x
        self.tile_y = tile_y

        # set the tiles to grey initially
        self.color = (177,177,177)
        
        # define a rectangle
        self.rect = pygame.Rect(self.tile_x, self.tile_y, self.tile_width, self.tile_height)
        
        # draw the rectangle
        pygame.draw.rect(Screen.screen, self.color, self.rect, 3)

    def check_mouse_over(self, mouse_x, mouse_y):
        if self.rect.collidepoint(mouse_x,mouse_y):
            return True
        else:
            return False
    
    def draw_tile(self,Screen, Player):
        pygame.draw.rect(Screen.screen, self.color, self.rect, 3)
        
    def redraw_tile(self,Screen, Player):
        if self.color == (177,177,177):
            pygame.draw.rect(Screen.screen, Player.click_color, self.rect, 3)
        else:
            pygame.draw.rect(Screen.screen, (255,0,0), self.rect, 3)
    
    def assign_color_tile(self,Screen,Player):
        if self.color == (177,177,177):
            self.color = Player.click_color
        else:
            self.color = self.color


class Board:
    def __init__(self, Screen, pieces_columns, pieces_rows):
        self.pieces_columns = pieces_columns
        self.pieces_rows = pieces_rows
        self.screen_width = Screen.screen_width
        self.screen_height = Screen.screen_height

        # finding the width of each box
        tile_width = self.screen_width / self.pieces_columns

        # finding the height of each box
        tile_height = self.screen_height / self.pieces_rows

        # findig the total number of rectangles
        total_rects = self.pieces_rows * self.pieces_columns

        self.tiles = []

        # creating the tiles in a loop
        for row in range(0, self.pieces_rows):
            self.column = []
            for column in range(0, self.pieces_columns):
                self.column.append(Tile(Screen, tile_width, tile_height, row*tile_width, tile_height*column))
            self.tiles.append(self.column)

class Player:
    def __init__(self, player_name, player_color):
        self.player_name = player_name
        self.player_color = player_color

        if self.player_color == "red":
            self.click_color = (255, 0, 0)
        if self.player_color == "blue":
            self.click_color = (0, 0, 255)
        if self.player_color == "green":
            self.click_color = (0, 255, 0)
        if self.player_color == "yellow":
            self.click_color = (247, 255, 0)
    
    # def piece_1(self, Piece):
        

    # create a new function in this class that will instantiate each piece for both of the players
# class Pieces:
#     def __init__(self, Board):
#         self.board = Board

#     def draw_piece_0(self,x,y):
#         # 5 in a straight line
#         self.piece0 = [self.board.tiles[x][y], self.board.tiles[x+1][y], self.board.tiles[x+2][y], self.board.tiles[x-1][y], self.board.tiles[x-2][y]]
#         self.piece0.is_used = 0
    
#     def draw_piece_1(self,x,y):
#         self.piece1 = [self.board.tiles[x]

def start_game(player1, player2):
    player_1 = Player(player1, 'blue')
    player_2 = Player(player2, 'red')
    screen = Screen(800, 800, 30)
    screen.start_display()
    board = Board(screen, 20, 20)
    while True:
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == MOUSEBUTTONUP:
                for x in range(0,board.pieces_rows):
                    for y in range(0,board.pieces_columns):
                        if board.tiles[x][y].check_mouse_over(mouse_x, mouse_y):
                            board.tiles[x][y].assign_color_tile(screen,player_1)
        for x in range(0,board.pieces_rows):
            for y in range(0,board.pieces_columns):
                board.tiles[x][y].draw_tile(screen,player_1)
                if board.tiles[x][y].check_mouse_over(mouse_x, mouse_y):
                    board.tiles[x][y].redraw_tile(screen,player_1)
        screen.display_update()

start_game('Shawn', 'Navi')



