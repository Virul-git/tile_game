import pygame



class Tile(pygame.Rect):
	
	List = []
	width, height = 40,40
	total_tiles = 1

	def __init__(self,x,y,Type):
		self.type = Type
		Tile.total_tiles += 1

		if Type == 'empty':
			self.walkable == True
		else:
			self.walkable == False
		pygame.Rect(self,(x,y),(Tile.width,Tile.height))
		Tile.List.append(self)
