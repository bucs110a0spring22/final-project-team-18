import pygame
from src import Piece
import random 

class Cube(pygame.sprite.Sprite):
 
    def __init__(self, row, column):
        self.size = 3
        self.row = row
        self.column = column 
        self.display_face = pygame.sprite.Group()
        self.sides = {
                "top":[], 
                "bottom":[], 
                "front":[], 
                "back":[],
                "left":[],
                "right":[]
            }
        for side in self.sides:
            current_row = 0 
            current_column = 100
            for i in range(self.row*self.column):
                p = Piece.Piece((current_row, current_column), side, self.get_side_color(side) )
                self.sides[side].append(p)
                current_row = (current_row + p.rect.w)
                if current_row >= (self.column*p.rect.h):
                    current_column = current_column + p.rect.h
                    current_row = 0
        self.display_face = pygame.sprite.Group(tuple(self.sides["front"]))
        
    def get_side_color(self, side):
        side_color = {
            "top":"white", 
            "bottom":"yellow", 
            "front":"red", 
            "back":"orange", 
            "left":"green", 
            "right":"blue"
        }
        return side_color[side]
   
    def moveUp(self, column):
        """
        description: shifts cube upward
        args: self, column
        return: nothing
        """
        top = self.sides["top"]
        back = self.sides["back"]
        bottom = self.sides["bottom"]
        front = self.sides["front"]
          
        if self.column < column < 0: return "Error: column not in range"
        for i in range(column, len(self.sides['front']), self.column):
            top[i], front[i], bottom[i], back[i] =  front[i], bottom[i], back[i], top[i]
        self.display_face = pygame.sprite.Group(tuple(self.sides["front"]))
         
    def moveDown(self, column):
        """
        description: shifts cube downward
        args: self, column
        return: nothing
        """
        top = self.sides["top"]
        back = self.sides["back"]
        bottom = self.sides["bottom"]
        front = self.sides["front"]
          
        if self.column < column < 0: return "Error: column not in range"
        for i in range(column, len(self.sides['front']), self.column):
            bottom[i], front[i], top[i], back[i] =  front[i], top[i], back[i], bottom[i]
        self.display_face = pygame.sprite.Group(tuple(self.sides["front"]))
        
    def moveLeft(self, row):
        """
        description: shifts cube left
        args: self, row
        return: nothing
        """
        front = self.sides["front"]
        left = self.sides["left"]
        back = self.sides["back"]
        right = self.sides["right"]
          
        if self.row < row < 0: return "Error: row not in range"
        for i in range(row, len(self.sides['front']), self.row):
            right[i], front[i], left[i], back[i] =  front[i], left[i], back[i], right[i]
        self.display_face = pygame.sprite.Group(tuple(self.sides["front"]))  

    def moveRight(self, row):
        """
        description: shifts cube right
        args: self, row
        return: nothing
        """
        front = self.sides["front"]
        left = self.sides["left"]
        back = self.sides["back"]
        right = self.sides["right"]
          
        if self.row < row < 0: return "Error: row not in range"
        for i in range(row, len(self.sides['front']), self.row):
            left[i], front[i], right[i], back[i] =  front[i], right[i], back[i], left[i]
        self.display_face = pygame.sprite.Group(tuple(self.sides["front"]))
      
    #shuffles cube
    def shuffle(self):
        num_moves = 20
        for i in range(random.randrange(num_moves)):
            if random.randrange(2):
                self.moveUp(i%self.column)
            if random.randrange(2):
                self.moveDown(i%self.column)
            if random.randrange(2):
                self.moveLeft(i%self.row)
            if random.randrange(2):
                self.moveRight(i%self.row)