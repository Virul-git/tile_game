import pygame
from characters import *
from tileC import Tile


def a_star(gameDisplay,Hero):
	
	N=-18
	S=18
	E=1
	W=-1

	NW=-19
	NE=-17
	SW=17
	SE=19

	def get_surrounding_tiles(base_node):
		
		array = (
			(base_node.number+N),
			(base_node.number+NE),
			(base_node.number+E),
			(base_node.number+SE),
			(base_node.number+S),
			(base_node.number+SW),
			(base_node.number+W),
			(base_node.number+NW),
			)
		#print array
		tiles = []

		for tile_number in array:

			surrounding_tile = Tile.get_tile(tile_number)

			if (surrounding_tile.walkable and surrounding_tile not in closed_list):
				tiles.append(surrounding_tile)

		return tiles

	def G():
		pass
	def H():
		for tile in Tile.List:
			tile.H = 10*(abs(tile.x-Hero.x) +abs(tile.y-Hero.y))/ Tile.width


	def F():
		pass
	
	def swap_tile(tile):
		open_list.remove(tile)
		closed_list.append(tile)


	for villan in Villans.List:
		open_list = []
		closed_list = []

		villan_tile = villan.get_tile()
		open_list.append(villan_tile)

		surrounding_nodes = get_surrounding_tiles(villan_tile)

		for node in surrounding_nodes:
			node.parent = villan_tile
			open_list.append(node)

		swap_tile(villan_tile)

		H()




			





