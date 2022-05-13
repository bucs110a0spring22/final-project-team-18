import pygame
import sys
from src import Cube
#import pygame_menu

class Controller:
  def __init__(self, width=640, height=480):
        pygame.init()
        pygame.font.init() #I think we only need this if we are going to display 'game over' or something 
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        # self.background.fill((0, 0, 0)) #set screen to black, to show outline of cube
        self.Cube = Cube.Cube(3, 3)
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
    self.backgroundstars = pygame.image.load("assets/background.png").convert()
    self.screen.blit(self.backgroundstars, (0, 0))
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
                    column = 1
                elif event.key == pygame.K_2:
                    column = 2
                elif event.key == pygame.K_3:
                    column = 3
                if event.key == pygame.K_4:
                    row = 4
                elif event.key == pygame.K_5:
                    row = 5
                elif event.key == pygame.K_6:
                    row = 6
                    
                if(event.key == pygame.K_UP):
                  self.Cube.moveUp(column)
                elif(event.key == pygame.K_DOWN):
                  self.Cube.moveDown(column)
                elif(event.key == pygame.K_LEFT):
                  self.Cube.moveLeft(row)
                elif(event.key == pygame.K_RIGHT):
                  self.Cube.moveRight(row)

        self.background.blit(self.screen, (0,0))
        self.Cube.display_face.draw(self.screen)
        pygame.display.flip()

  """
description: loop with all events, determines what loop it is in depending on what state it is in
args: self
return: nothing
    """