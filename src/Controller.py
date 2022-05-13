import pygame
import sys
from src import Cube
#import pygame_menu
from src import Piece

class Controller:
  def __init__(self, width=640, height=480):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((0, 0, 0)) #set screen to black, to show outline of cube
        self.Cube = Cube.Cube(3, 3)
        #self.displayFace = Piece.Piece(row, column)
        #self.Piece = Piece.Piece(3, 3, "red")
        self.state = "GAME"
        """
	  description: initialize the controller
	  args: self,width,height
  	return: nothing
        """
        #just testing display
        #self.image = pygame.Surface([50,50]) 
        #self.image.fill((255,255,255))
       # self.rect = self.image.get_rect()
    
  def mainLoop(self):
      if(self.state == "GAME"):    
        self.gameLoop()

  
  def gameLoop(self):
   # self.display = pygame.sprite.Group()
    #self.display.add(self.Cube)
    self.allSprites = pygame.sprite.Group(self.Cube.display_face)	

    
    #width, height = pygame.display.get_window_size()
    #menu = pygame_menu.Menu("", width-20, height-20)
    #menu.add.button('Play', self.Cube.shuffle, self, align=pygame_menu.locals.ALIGN_LEFT)
    #self.add.label("Press shuffle button to shuffle the rubik cube", max_char=-1, font_size=20)
    #myfont = pygame.font.SysFont("monospace", 15)
    #shuffle_label = myfont.render("Press play button to shuffle the rubik cube", 1, (255,255,0))
    #self.screen.blit(shuffle_label, (0, 750))
    self.Cube.shuffle()
    while self.state == "GAME":

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                #each key fires a single event, so you cannot have two keys in the same event
                # your event will never fire
                #maybe change the second key to 1,2,3 and add labels?
                if event.key == pygame.K_1:
                    selected = 1
                elif event.key == pygame.K_2:
                    selected = 2
                elif event.key == pygame.K_3:
                    selected = 3
                    
                if(event.key == pygame.K_UP):
                  self.Cube.moveUp(selected)
                elif(event.key == pygame.K_DOWN):
                  self.Cube.moveDown(selected)
                elif(event.key == pygame.K_LEFT):
                  self.Cube.moveLeft(selected)
                elif(event.key == pygame.K_RIGHT):
                  self.Cube.moveRight(selected)


        self.background.blit(self.screen, (0,0))
        self.Cube.display_face.draw(self.screen)
        pygame.display.flip()

      
  """
description: loop with all events, determines what loop it is in depending on what state it is in
args: self
return: nothing
    """