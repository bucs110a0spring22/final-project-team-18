import pygame

class Piece(pygame.sprite.Sprite):
  def __init__(self, x, y, color):
    super().__init__()
    pygame.sprite.Sprite.__init__(self)
    # self.image = pygame.image.load("assets/f'{color}Sq.png").convert_alpha()  (original)
    #self.image = pygame.image.load("assets/" + color + "Sq.png").convert_alpha()
    self.sprites = []
    #self.sprites.append(pygame.image.load("assets/" + color + "Sq.png").convert_alpha())
    self.image = pygame.image.load(color).convert_alpha()
    #self.current_sprite = 0 
    #self.image = self.sprites[self.current_sprite]
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.correct_face = color
    self.current_face = color
    self.size = 3

#sets up 6 faces of the cube 
 # def topFace(self):
    
  
   #self.botFace = topRow + midRow + botRow
    
    #return self.botFace
  
 # def leftFace(self):
    #topRow = []
    #for i in range(self.size):
      #topRow.append("white piece ")
    #midRow = []
    #for i in range(self.size):
      #midRow.append("white piece ")
    #botRow = []
    #for i in range(self.size):
      #botRow.append("white piece ")

    #self.lFace = []
    #self.lFace = topRow + midRow + botRow
    
    #return self.lFace
  
  #def rightFace(self):
    #topRow = []
    #for i in range(self.size):
      #topRow.append("blue piece ")
    #midRow = []
    #for i in range(self.size):
      #midRow.append("blue piece ")
    #botRow = []
    #for i in range(self.size):
      #botRow.append("blue piece ")

    #self.rFace = []
   # self.rFace = topRow + midRow + botRow
    
    #return self.rFace
  
  #def backFace(self):
    #topRow = []
   # for i in range(self.size):
      #topRow.append("orange piece ")
    #midRow = []
    #for i in range(self.size):
     # midRow.append("orange piece ")
    #botRow = []
    #for i in range(self.size):
      #botRow.append("orange piece ")

    #self.bacFace = []
    #self.bacFace = topRow + midRow + botRow
    
    #return self.bacFace