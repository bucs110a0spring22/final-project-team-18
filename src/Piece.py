import pygame

class Piece(pygame.sprite.Sprite):
  def __init__(self, x, y, color):
    super().__init__()
    #issue is that strings are immutable 
    # self.image = pygame.image.load("assets/f'{color}Sq.png").convert_alpha()
    self.image = pygame.image.load("assets/" + color + "Sq.png")
    self.image2 = pygame.image.load("assets/{1}Sq.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.correct_face = color
    self.current_face = color
    self.size = 3

#sets up 6 faces of the cube 
   
  def topFace(self, column):
    
    topRow = []
    for i in range(self.size):
      topRow.append("green piece ")
    midRow = []
    for i in range(self.size):
      midRow.append("green piece ")
    botRow = []
    for i in range(self.size):
      botRow.append("green piece ")

    self.tFace = []
    self.tFace = topRow + midRow + botRow
    
    return self.tFace #each face is returned as a list so it can be manipulated (hopefully)

  def frontFace(self):
    topRow = []
    for i in range(self.size):
      topRow.append("yellow piece ")
    midRow = []
    for i in range(self.size):
      midRow.append("yellow piece ")
    botRow = []
    for i in range(self.size):
      botRow.append("yellow piece ")

    self.fFace = []
    self.fFace = topRow + midRow + botRow
    
    return self.fFace
  
  def bottomFace(self):
    topRow = []
    for i in range(self.size):
      topRow.append("red piece ")
    midRow = []
    for i in range(self.size):
      midRow.append("red piece ")
    botRow = []
    for i in range(self.size):
      botRow.append("red piece ")

    self.botFace = []
    self.botFace = topRow + midRow + botRow
    
    return self.botFace
  
  def leftFace(self):
    topRow = []
    for i in range(self.size):
      topRow.append("white piece ")
    midRow = []
    for i in range(self.size):
      midRow.append("white piece ")
    botRow = []
    for i in range(self.size):
      botRow.append("white piece ")

    self.lFace = []
    self.lFace = topRow + midRow + botRow
    
    return self.lFace
  
  def rightFace(self):
    topRow = []
    for i in range(self.size):
      topRow.append("blue piece ")
    midRow = []
    for i in range(self.size):
      midRow.append("blue piece ")
    botRow = []
    for i in range(self.size):
      botRow.append("blue piece ")

    self.rFace = []
    self.rFace = topRow + midRow + botRow
    
    return self.rFace
  
  def backFace(self):
    topRow = []
    for i in range(self.size):
      topRow.append("orange piece ")
    midRow = []
    for i in range(self.size):
      midRow.append("orange piece ")
    botRow = []
    for i in range(self.size):
      botRow.append("orange piece ")

    self.bacFace = []
    self.bacFace = topRow + midRow + botRow
    
    return self.bacFace