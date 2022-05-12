import pygame
from src import Cube
import pygame_menu
from src import Piece

class Controller:
  def __init__(self, width=800, height=800, row=3, column=3):
        pygame.init()
        pygame.font.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((0, 0, 0)) #set screen to black, to show outline of cube
        self.Cube = Cube.Cube(3,3)
        self.Piece = Piece.Piece(3,3,"green")
        self.state = "GAME"
        run = True
        player_rect = pygame.rect.Rect(176, 134, 17, 17)
        player_dragging = False

        """
	  description: initialize the controller
	  args: self,width,height
  	return: nothing
        """
  def mainLoop(self):
    while True:
      if(self.state == "GAME"):
        self.gameLoop()
      elif(self.state == "GAMEOVER"):
        self.gameOver()
            
      
##double click or one click for row or column
# if pygame 

      
    
#https://stackoverflow.com/questions/29640685/how-do-i-detect-collision-in-pygame
  #-collusion related will get back to -connie


  
  """
	  description: loop with all events, determines what loop it is in depending on what state it is in
	  args: self
  	return: nothing
        """
  def gameloop(self):
    self.add.button('Shuffle', self.cube.shuffle, self, align=pygame_menu.locals.ALIGN_LEFT)
    # self.add.label("Press shuffle button to shuffle the rubik cube", max_char=-1, font_size=20)
    myfont = pygame.font.SysFont("monospace", 15)
    shuffle_label = myfont.render("Press shuffle button to shuffle the rubik cube", 1, (255,255,0))
    self.screen.blit(shuffle_label, (0, 750))
    while self.state == "GAME":
      self.cube()
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              exit()


            #moving the cube
          # elif event.type == pygame.MOUSEBUTTONDOWN:
          #   if event.button == 1:
          #       player_dragging = True
          #       Cube.moveUp(self,1,1)
          #   if event.button == 3:
          #       player_dragging = True
          #       Cube.moveDown(self,1,1)
                
          # elif event.type == pygame.MOUSEBUTTONUP:
          #   player_dragging = False
              
      Cube.display_face.draw(self.screen) #displays cube
