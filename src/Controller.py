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
        self.Cube = Cube()
        self.state = "GAME"
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
        self.menu()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if start_button.checkforinput(MENU):
          self.state = "GAME"
        
        
        """
	  description: loop with all events, determines what loop it is in depending on what state it is in
	  args: self
  	return: nothing
        """
  def menu(elf):
    pygame.display.set_caption("Menu")
    mouse.enabled(True)
    while self.state == "MENU":
      menu = pygame_menu.Menu("Welcome to Rubix Cube!",800,600,theme=pygame_menu.themes.THEME_BLUE)
      if state == "GAME":
        pygame_menu.events.CLOSE
      
      #has bare bones buttons and words

  def gameloop(self):
    while self.state == "GAME":
      self.background.fill((255, 255, 255)) #meant to fill over the menu
      #event loop
      message = myfont.render('Press space to restart cube.', False, (0, 0, 0))
      self.screen.blit(message, (self.width / 2, self.height / 2))
      for event in pygame.event.get():
        if event.type == pygame.K_SPACE:
        gamerestart()
        elif event.type == pygame.QUIT:
          sys.exit()


          """
	  description: restarts cube 
	  args: self
  	return: nothing
        """  
  def gamerestart(self): 
    

 