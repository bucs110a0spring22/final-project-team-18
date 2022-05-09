import pygame
import pygame_menu
from src import Piece
from src import Cube
from pygame_menu.widgets.widget.mywidget import MyWidget


class Controller:
  def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((55, 55, 55))
        self.font_name = '8 BIT-WONDER.TTF'

  def mainLoop(self):
    while (self.state == "GAME"):
        self.gameLoop()
                      
  def menuloop(elf):
    pygame.display.set_caption("Menu")
    mouse enabled(True)
    while self.state == "MENU"
      menu = pygame_menu.Menu("Welcome to Rubix Cube!")
      if state == "GAME"
      pygame_menu.events.CLOSE

  def gameloop(self):
    while self.state == "GAME"
      #event loop
      message = myfont.render('Press space to restart cube.', False, (0, 0, 0))
      self.screen.blit(message, (self.width / 2, self.height / 2))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      for event in pygame.event.get():
        if event.type == pygame.K_SPACE:
          gamerestart()
      #update data

      #redraw
    
  def Restart(self):
    while self.state = "GAME"
      "Set cube to restart code"
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()

