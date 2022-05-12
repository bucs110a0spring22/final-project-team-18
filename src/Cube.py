import pygame
from src import Piece
import random 

class Cube(pygame.sprite.Sprite):
  def __init__(self, row, column):
    self.row = row
    self.column = column
    current_row = 0
    current_column = 0
    self.pieces = pygame.sprite.Group()
    sides = ["white", "yellow", "red", "orange", "green", "blue"]
    for color in sides:
        for i in range(row*column):
           p = Piece.Piece(current_row, current_column, color)
           self.pieces.add(p)
           current_row = (current_row + 10)
           if current_row == (self.column*10):
               current_column = current_column + 10
               current_row = 0
             
    self.topFace = pygame.sprite.Group()
    for i in range(row*column):
      p = Piece.Piece(current_row, current_column, 'assets/whiteSq.png')
      self.topFace.add(p)
      current_row = (current_row + 10)
      if current_row == (self.column*10):
        current_column = current_column + 10
        current_row = 0
        
    self.bottomFace = pygame.sprite.Group()
    for i in range(row*column):
      p = Piece.Piece(current_row, current_column, 'assets/yellowSq.png')
      self.bottomFace.add(p)
      current_row = (current_row + 10)
      if current_row == (self.column*10):
        current_column = current_column + 10
        current_row = 0
        
    self.displayFace = pygame.sprite.Group()
    for i in range(row*column):
      p = Piece.Piece(current_row, current_column, 'assets/redSq.png')
      self.displayFace.add(p)
      current_row = (current_row + 10)
      if current_row == (self.column*10):
        current_column = current_column + 10
        current_row = 0
        
    self.backFace = pygame.sprite.Group()
    for i in range(row*column):
      p = Piece.Piece(current_row, current_column, 'assets/orangeSq.png')
      self.backFace.add(p)
      current_row = (current_row + 10)
      if current_row == (self.column*10):
        current_column = current_column + 10
        current_row = 0
        
    self.leftFace = pygame.sprite.Group()
    for i in range(row*column):
      p = Piece.Piece(current_row, current_column, 'assets/greenSq.png')
      self.leftFace.add(p)
      current_row = (current_row + 10)
      if current_row == (self.column*10):
        current_column = current_column + 10
        current_row = 0
        
    self.rightFace = pygame.sprite.Group()
    for i in range(row*column):
      p = Piece.Piece(current_row, current_column, 'assets/blueSq.png')
      self.rightFace.add(p)
      current_row = (current_row + 10)
      if current_row == (self.column*10):
        current_column = current_column + 10
        current_row = 0

#do these methods not work? 
#anything that I comment out, idk if it will work or not, just trying to get rid of stuff to see 'something'
        #slay got it
        
  #def topFace(self,row,column):
    #current_row = 0
    #current_column = 0
    #for i in range(row*column):
      #p = Piece.Piece(current_row, current_column, "white")
      #self.pieces.add(p)
      #current_row = (current_row + 10)
      #if current_row == (self.column*10):
        #current_column = current_column + 10
        #current_row = 0
        
  #def bottomFace(self,row,column):
    #current_row = 0
    #current_column = 0
    #for i in range(row*column):
      #p = Piece.Piece(current_row, current_column, 'assets/yellowSq.png')
      #self.pieces.add(p)
      #current_row = (current_row + 10)
      #if current_row == (self.column*10):
        #current_column = current_column + 10
        #current_row = 0

  #def frontFace(self,row,column):
    #current_row = 0
    #current_column = 0
    #for i in range(row*column):
      #p = Piece.Piece(current_row, current_column, 'assets/redSq.png')
      #self.pieces.add(p)
      #current_row = (current_row + 10)
      #if current_row == (self.column*10):
        #current_column = current_column + 10
        #current_row = 0

  #def backFace(self,row,column):
    #current_row = 0
    #current_column = 0
    #for i in range(row*column):
      #p = Piece.Piece(current_row, current_column, 'assets/orangeSq.png')
      #self.pieces.add(p)
      #current_row = (current_row + 10)
      #if current_row == (self.column*10):
        #current_column = current_column + 10
        #current_row = 0
  
  #def leftFace(self,row,column):
    #current_row = 0
    #current_column = 0
    #for i in range(row*column):
      #p = Piece.Piece(current_row, current_column, 'assets/greenSq.png')
      #self.pieces.add(p)
      #current_row = (current_row + 10)
      #if current_row == (self.column*10):
        #current_column = current_column + 10
        #current_row = 0

  #first line original wrote: self.rightFace(self,row,column):
  #def rightFace(self,row,column):
    #current_row = 0
    #current_column = 0
    #for i in range(row*column):
      #p = Piece.Piece(current_row, current_column, 'assets/blueSq.png')
      #self.pieces.add(p)
      #current_row = (current_row + 10)
      #if current_row == (self.column*10):
        #current_column = current_column + 10
        #current_row = 0
      
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