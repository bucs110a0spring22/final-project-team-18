import pygame
from src import Cube

class Controller:
  def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
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
    self.controls = pygame.image.load("assets/presswforcontrols.png").convert()
    self.screen.blit(self.controls, (0, 0))
    self.allSprites = pygame.sprite.Group(self.Cube.display_face)
    self.Cube.shuffle()
    while self.state == "GAME":

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                  print("Welcome to Rubik Cube! Press either 1, 2, or 3 to determine the column you want to turn. Press the up, down, right, and left keys to turn the cube.")
                elif event.key == pygame.K_1:
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