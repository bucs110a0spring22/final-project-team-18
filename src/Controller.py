import pygame
import sys
from src import Cube
import pygame_menu
from src import Piece

class Controller:
  def __init__(self, width=640, height=480, row=3, column=3):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((0, 0, 0)) #set screen to black, to show outline of cube
        self.Cube = Cube.Cube(row,column)
        self.Piece = Piece.Piece(3,3,"green")
        self.state = "GAME"

        """
	  description: initialize the controller
	  args: self,width,height
  	return: nothing
        """
  def mainLoop(self):
      if(self.state == "GAME"):
        self.gameLoop()

  
  def gameLoop(self):
    width, height = pygame.display.get_window_size()
    menu = pygame_menu.Menu("", width-20, height-20)
    menu.add.button('Play', self.Cube.shuffle, self, align=pygame_menu.locals.ALIGN_LEFT)
    #self.add.label("Press shuffle button to shuffle the rubik cube", max_char=-1, font_size=20)
    myfont = pygame.font.SysFont("monospace", 15)
    shuffle_label = myfont.render("Press play button to shuffle the rubik cube", 1, (255,255,0))
    self.screen.blit(shuffle_label, (0, 750))
    while self.state == "GAME":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()
          if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_UP and event.key == pygame.K_l):
              self.Cube.moveUp()
            elif(event.key == pygame.K_UP and event.key == pygame.K_c):
              self.Cube.moveUp()
            elif(event.key == pygame.K_UP and event.key == pygame.K_r):
              self.Cube.moveUp()
            elif(event.key == pygame.K_DOWN and event.key == pygame.K_l):
              self.Cube.moveDown()
            elif(event.key == pygame.K_DOWN and event.key == pygame.K_c):
              self.Cube.moveDown()
            elif(event.key == pygame.K_DOWN and event.key == pygame.K_r):
              self.Cube.moveDown()
            elif(event.key == pygame.K_LEFT and event.key == pygame.K_t):
              self.Cube.moveLeft()
            elif(event.key == pygame.K_LEFT and event.key == pygame.K_m):
              self.Cube.moveLeft()
            elif(event.key == pygame.K_LEFT and event.key == pygame.K_b):
              self.Cube.moveLeft()
            elif(event.key == pygame.K_RIGHT and event.key == pygame.K_t):
              self.Cube.moveRight()
            elif(event.key == pygame.K_RIGHT and event.key == pygame.K_m):
              self.Cube.moveRight()
            elif(event.key == pygame.K_RIGHT and event.key == pygame.K_b):
              self.Cube.moveRight()
              
        self.Cube.displayFace.draw(self.screen)
      
        """
	  description: loop with all events, determines what loop it is in depending on what state it is in
	  args: self
  	return: nothing
        """