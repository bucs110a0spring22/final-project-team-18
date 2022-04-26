from Piece import Piece

class Cube:
  def __init__(self, size):
    self.size = size
    self.pieces = []
    self.shuffle = []
    
  def createCube(self, size):
    for a in range(size):
      for b in range(size):
        for c in range(size):
          self.pieces(Piece)