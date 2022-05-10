import pygame
from src import Cube
import pygame_menu
from src import Piece

class Controller:
  def __init__(self, width=800, height=800):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((0, 0, 0)) #set screen to black, to show outline of cube
        self.font_name = '8 BIT-WONDER.TTF'
        self.Cube = pygame.sprite.Group()
        self.piece = piece.Hero("blueSq", 50, 80, "assets/blueSq.png")
        self.piece = piece.Hero("greenSq", 50, 80, "assets/greenSq.png")
        self.piece = piece.Hero("orangeSq", 50, 80, "assets/orangeSq.png")
        self.piece = piece.Hero("redSq", 50, 80, "assets/redSq.png")
        self.piece = piece.Hero("whiteSq", 50, 80, "assets/whiteSq.png")
        self.piece = piece.Hero("yellowSq", 50, 80, "assets/yellowSq.png")
        self.piece = Piece()
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
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          exit()

        """
	  description: loop with all events, determines what loop it is in depending on what state it is in
	  args: self
  	return: nothing
        """
  def gameloop(self):
    self.add.button('Shuffle', self.cube.shuffle, self, align=pygame_menu.locals.ALIGN_LEFT)
    self.add.label("Press shuffle button to shift the rubik cube", max_char=-1, font_size=20)
    while self.state == "GAME":
      self.cube()
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              exit()



#not sure how to put cube in
#not sure what error is 
#controls

    
  # def gameloop(self):
  #   while self.state == "GAME":
  #     for event in pygame.event.get():
  #       if event.type == pygame.K_SPACE:
  #       gamerestart()
  #       elif event.type == pygame.QUIT:
  #         sys.exit()
