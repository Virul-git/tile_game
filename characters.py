import pygame
from tileC import Tile


class character(pygame.Rect):
	
	width=40
	height=40

	def __init__(self,x,y):
		pygame.Rect.__init__(self,x,y,character.width,character.height)
	
	def get_number(self):
		return ((self.x/width)+Tile.H)+((self.y/height)+Tile.V)
	
	def get_tile(self):
		return Tile.get_tile(self.get_number())


class Villans(character):
	List = []

	def __init__(self,x,y):
		character.__init__(self,x,y)
		Villans.List.append(self)

	@staticmethod
	def draw_villans(self,gameDisplay):
		for Villan in Villans.List:
			pygame.draw.rect(gameDisplay,[200,30,80],Villan)


class Survivor(character):
	
	def __init__(self,x,y):
		character.__init__(self,x,y)

	def draw_survivor(self,gameDisplay):
		r= self.width/2
		pygame.draw.circle(gameDisplay,[80,250,160],(self.x+r,self.y+r),r)
	



