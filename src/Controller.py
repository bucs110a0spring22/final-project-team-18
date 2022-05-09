import pygame
from src import Piece
from src import Cube
from pygame_menu.widgets.widget.mywidget import MyWidget
from pygame_widgets.button import Button


class Controller:
  def __init__(self, width=800, height=800):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((0, 0, 0)) #set screen to black, to show outline of cube
        self.font_name = '8 BIT-WONDER.TTF'
        start_img = pygame.image.load('assets/start_button.png').convert.alpha

        """
	  description: initialize the controller, initalizes the start buttons
	  args: self,width,height
  	return: nothing
        """

  def mainLoop(self):
    while True:
      if (self.state == "GAME"):
        self.gameLoop()
      elif (self.state == "MENU"):
        
        """
	  description: loop with all events, determines what loop it is in depending on what state it is in
	  args: self
  	return: nothing
        """
  def menu(self):
    pygame.display.set_caption("Menu")
    mouse.enabled(True)
    while self.state == "MENU"
      menu = pygame_menu.Menu("Welcome to Rubix Cube!")
      start_button = button(screen,100,100,100,100,(hoverColour = 150,0,0),onClick = gameloop)
      if state == "GAME"
        pygame_menu.events.CLOSE
      #has bare bones buttons and words
        """
	  description: gives the frontend code for the menu screen
	  args: self
  	return: nothing
        """

  def gameloop(self):
    while self.state == "GAME"
      self.background.fill((255, 255, 255)) #meant to fill over the menu
      #event loop
      message = myfont.render('Press space to restart cube.', False, (0, 0, 0))
      self.screen.blit(message, (self.width / 2, self.height / 2))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
      for event in pygame.event.get():
        if event.type == pygame.K_SPACE:
          gamerestart()
        """
	  description: gives the frontend for the gameloop, and controls (not added yet)
	  args: self
  	return: nothing
        """
  def gamerestart(self): 
    while self.state = "GAME"
      set ""
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              sys.exit()
        """
	  description: restarts cube so player can start with a cube that isn't shuffled
	  args: self
  	return: nothing
        """