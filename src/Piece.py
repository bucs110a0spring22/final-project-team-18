import pygame

class Piece(pygame.sprite.Sprite):
  def __init__(self, pos, face, color):
    super().__init__()
    self.image = pygame.image.load("assets/" + color + "Sq.png").convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.topleft = pos
    self.correct_face = color
    self.current_face = face