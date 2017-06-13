import pygame
import my_text

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)


class Tile(pygame.Rect):
	
	List = []
	width, height = 40,40
	total_tiles = 1
	H, V = 1,18

	def __init__(self,x,y,Type):
		
		self.parent = None
		self.G, self.H,self.F = 0,0,0
		
		self.type = Type
		self.number = Tile.total_tiles
		Tile.total_tiles += 1

		if Type == 'empty':
			self.walkable = True
		else:
			self.walkable = False
		pygame.Rect.__init__(self,(x,y),(Tile.width,Tile.height))
		Tile.List.append(self)

	@staticmethod
	def get_tile(number):
		for tile in Tile.List:
			if tile.number == number:
				return tile
	@staticmethod
	def draw_tiles(gameDisplay):
		for tile in Tile.List:
			if not (tile.type == 'empty'):
				pygame.draw.rect(gameDisplay,blue,tile)

			if tile.G != 0:
				my_text.text_display(gameDisplay,tile.G,tile.x,tile.y+20,color=red)
			if tile.H != 0:
				my_text.text_display(gameDisplay,tile.H,tile.x+20,tile.y,color=blue)
			if tile.F != 0:
				my_text.text_display(gameDisplay,tile.F,tile.x+20,tile.y+20,color=green)		
			
			my_text.text_display(gameDisplay,tile.number,tile.x,tile.y)
