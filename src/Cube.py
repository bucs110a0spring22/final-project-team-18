import pygame
from Piece import Piece
import random 

class Cube:
  def __init__(self, row, column, pc, img_file):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(img_file).convert_alpha()
    self.rect = self.image.get_rect()
    self.row = row
    self.column = column
    self.size = 3
    self.pc = Piece.Piece()

  #rotates whole cube  
  def rotateUp(self, angle):
    self.rect = pygame.transform.rotate(self.rect, 90)
  def rotateDown(self, angle):
    self.rect = pygame.transform.rotate(self.rect, 270)
  def rotateLeft(self, angle):
    self.rect = pygame.transform.rotate(self.rect, 180)
  def rotateRght(self, angle):
    self.rect = pygame.transform.rotate(self.rect, 0)

  #move = move individual row/column
    
  #moves individual rows/columns
  def moveUp(self, column, numMoves):
    moves = 0
    while moves < numMoves:
      if column < 0: return "Error: column not in range"
      if column > self.size: return "Error: column not in range"
    
        #rotates columns up one face (front colors move to top, top to back, etc.)
      temp=[]
      for i in range(len(self.pc.tFace)):#holds top face
          temp[i]=self.pc.tFace[i]
      for i in range(self.size):#front to top
        x=column
        if column == i:
          for i in range(self.size):
            self.pc.tFace[x] = self.pc.fFace[x]
            x+=self.size
      for i in range(self.size):#bottom to front
        x=column
        if column == i:
          for i in range(self.size):
            self.pc.fFace[x] = self.pc.botFace[x]
            x+=self.size
      for i in range(self.size):#back to bottom
        x=column
        if column == i:
          for i in range(self.size):
            self.pc.botFace[x] = self.pc.bacFace[x]
            x+=self.size
      for i in range(self.size):#top(temp list) to back
        x=column
        if column == i:
          for i in range(self.size):
            self.pc.bacFace[x] = temp[x]
            x+=self.size
      
  
      if column == 0:#rotates left face
        holder=[]
        x=0
        y=self.size * 2
        z=0
        a=self.size-1
        b=self.size-1
        for i in range(len(self.pc.lFace)):
          holder[i]=self.pc.lFace[i]
        for i in range(self.size):#top to left
          self.pc.lFace[x]=holder[a-i]
          x+=self.size

        for i in range(self.size):#left to bottom
          self.pc.lFace[y]=holder[z]
          z+=self.size
          y+=1
        for i in range(self.size):#bottom to right
          self.pc.lFace[a]=holder[len(self.pc.lFace)-i]
          x+=1
          a+=self.size  
        for i in range(self.size):#right to top
          self.pc.lFace[i]=holder[b]
          b+=self.size 
      
      elif column == 2:#rotates right face
        holder=[]
        x=0
        y=self.size * 2
        z=0
        a=self.size-1
        b=self.size-1
        for i in range(len(self.pc.rFace)):
          holder[i]=self.pc.rFace[i]
        for i in range(self.size):#top to right
          self.pc.rFace[a]=holder[i]
          a+=self.size

        for i in range(self.size):#right to bottom
          self.pc.rFace[y]=holder[len(self.pc.rFace)-i]
          b+=self.size
          y+=1
        for i in range(self.size):#bottom to left
          self.pc.rFace[x]=holder[a]
          a+=1
          x+=self.size  
        for i in range(self.size):#left to top
          self.pc.rFace[i]=holder[b]
          b+=self.size 
    

    
        
        
      
  def moveDown(self, column, numMoves):
    moves = 0
    while moves < numMoves:
      if column < 0: return "Error: column not in range"
      if column > self.size: return "Error: column not in range"
    
        #rotates columns down one face (front colors move to bottom, bottom to back, etc.)
      temp=[]
      for i in range(len(self.pc.tFace)):#holds top face
          temp[i]=self.pc.tFace[i]
      for i in range(self.size):#front to bottom
        x=column
        if column == i:
          for i in range(self.size):
            self.pc.botFace[x] = self.pc.fFace[x]
            x+=self.size
      for i in range(self.size):#bottom to back
        x=column
        if column == i:
          for i in range(self.size):
            self.pc.bacFace[x] = self.pc.botFace[x]
            x+=self.size
      for i in range(self.size):#back to top
        x=column
        if column == i:
          for i in range(self.size):
            self.pc.tFace[x] = self.pc.bacFace[x]
            x+=self.size
      for i in range(self.size):#top(temp list) to front
        x=column
        if column == i:
          for i in range(self.size):
            self.pc.fFace[x] = temp[x]
            x+=self.size
      
  
      if column == 0:#rotates left face
        holder=[]
        x=0
        y=self.size * 2
        z=0
        a=self.size-1
        b=self.size-1
        for i in range(len(self.pc.lFace)):
          holder[i]=self.pc.lFace[i]
        for i in range(self.size):#top to right
          self.pc.lFace[a]=holder[i]
          a+=self.size

        for i in range(self.size):#right to bottom
          self.pc.lFace[y]=holder[len(self.pc.lFace)-i]
          b+=self.size
          y+=1
        for i in range(self.size):#bottom to left
          self.pc.lFace[x]=holder[a]
          a+=1
          x+=self.size  
        for i in range(self.size):#left to top
          self.pc.lFace[i]=holder[b]
          b+=self.size
      
      elif column == 2:#rotates right face
        holder=[]
        x=0
        y=self.size * 2
        z=0
        a=self.size-1
        b=self.size-1
        for i in range(len(self.pc.rFace)):
          holder[i]=self.pc.lFace[i]
        for i in range(self.size):#top to left
          self.pc.rFace[x]=holder[a-i]
          x+=self.size

        for i in range(self.size):#left to bottom
          self.pc.rFace[y]=holder[z]
          z+=self.size
          y+=1
        for i in range(self.size):#bottom to right
          self.pc.rFace[a]=holder[len(self.pc.rFace)-i]
          x+=1
          a+=self.size  
        for i in range(self.size):#right to top
          self.pc.rFace[i]=holder[b]
          b+=self.size  
  

  def moveLeft(self, row, numMoves):
    moves = 0
    while moves < numMoves:
      if row < 0: return "Error: row not in range"
      if row > self.size: return "Error: row not in range"
    
        #rotates rows left one face (front colors move to left, left to back, etc.)
      temp=[]
      for i in range(len(self.pc.rFace)):#holds right face
          temp[i]=self.pc.rFace[i]
      for i in range(self.size):#front to left
        if row == i:
          for i in range(self.size):
            self.pc.lFace[i] = self.pc.fFace[i]
      for i in range(self.size):#left to back
        if row == i:
          for i in range(self.size):
            self.pc.bacFace[i] = self.pc.lFace[i]
      for i in range(self.size):#back to right
        if row == i:
          for i in range(self.size):
            self.pc.rFace[i] = self.pc.bacFace[i]
      for i in range(self.size):#right(temp list) to front
        if row == i:
          for i in range(self.size):
            self.pc.rFace[i] = temp[i]
      
  
      if row == 0:#rotates top face
        holder=[]
        x=0
        y=self.size * 2
        z=0
        a=self.size-1
        b=self.size-1
        for i in range(len(self.pc.tFace)):
          holder[i]=self.pc.tFace[i]
        for i in range(self.size):#top to right
          self.pc.tFace[a]=holder[i]
          a+=self.size

        for i in range(self.size):#right to bottom
          self.pc.tFace[y]=holder[len(self.pc.tFace)-i]
          b+=self.size
          y+=1
        for i in range(self.size):#bottom to left
          self.pc.tFace[x]=holder[a]
          a+=1
          x+=self.size  
        for i in range(self.size):#left to top
          self.pc.tFace[i]=holder[b]
          b+=self.size 
      
      elif row == 2:#rotates bottom face
        holder=[]
        x=0
        y=self.size * 2
        z=0
        a=self.size-1
        b=self.size-1
        for i in range(len(self.pc.botFace)):
          holder[i]=self.pc.botFace[i]
        for i in range(self.size):#top to left
          self.pc.botFace[x]=holder[a-i]
          x+=self.size

        for i in range(self.size):#left to bottom
          self.pc.botFace[y]=holder[z]
          z+=self.size
          y+=1
        for i in range(self.size):#bottom to right
          self.pc.botFace[a]=holder[len(self.pc.botFace)-i]
          x+=1
          a+=self.size  
        for i in range(self.size):#right to top
          self.pc.botFace[i]=holder[b]
          b+=self.size
  def moveRight(self, row, numMoves):
    moves = 0
    while moves < numMoves:
      if row < 0: return "Error: row not in range"
      if row > self.size: return "Error: row not in range"
    
        #rotates rows right one face (front colors move to right, right to back, etc.)
      temp=[]
      for i in range(len(self.pc.lFace)):#holds left face
          temp[i]=self.pc.lFace[i]
      for i in range(self.size):#front to right
        if row == i:
          for i in range(self.size):
            self.pc.rFace[i] = self.pc.fFace[i]
      for i in range(self.size):#right to back
        if row == i:
          for i in range(self.size):
            self.pc.bacFace[i] = self.pc.rFace[i]
      for i in range(self.size):#back to left
        if row == i:
          for i in range(self.size):
            self.pc.lFace[i] = self.pc.bacFace[i]
      for i in range(self.size):#left(temp list) to front
        if row == i:
          for i in range(self.size):
            self.pc.fFace[i] = temp[i]
      
  
      if row == 0:#rotates top face
        holder=[]
        x=0
        y=self.size * 2
        z=0
        a=self.size-1
        b=self.size-1
        for i in range(len(self.pc.tFace)):
          holder[i]=self.pc.tFace[i]
        for i in range(self.size):#top to left
          self.pc.tFace[x]=holder[a-i]
          x+=self.size

        for i in range(self.size):#left to bottom
          self.pc.tFace[y]=holder[z]
          z+=self.size
          y+=1
        for i in range(self.size):#bottom to right
          self.pc.tFace[a]=holder[len(self.pc.tFace)-i]
          x+=1
          a+=self.size  
        for i in range(self.size):#right to top
          self.pc.tFace[i]=holder[b]
          b+=self.size 
      
      elif row == 2:#rotates bottom face
        holder=[]
        x=0
        y=self.size * 2
        z=0
        a=self.size-1
        b=self.size-1
        for i in range(len(self.pc.botFace)):
          holder[i]=self.pc.botFace[i]
        for i in range(self.size):#top to right
          self.pc.botFace[a]=holder[i]
          a+=self.size

        for i in range(self.size):#right to bottom
          self.pc.botFace[y]=holder[len(self.pc.botFace)-i]
          b+=self.size
          y+=1
        for i in range(self.size):#bottom to left
          self.pc.botFace[x]=holder[a]
          a+=1
          x+=self.size  
        for i in range(self.size):#left to top
          self.pc.botFace[i]=holder[b]
          b+=self.size
      
  #shuffles cube
  def shuffle(self):
    for i in range(3):
      self.moveUp(i, random())
      self.moveDown(i, random())
      self.moveLeft(i, random())
      self.moveRight(i, random())


      
  
      