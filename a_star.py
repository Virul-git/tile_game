import pygame
from characters import *
from tileC import Tile


def a_star():
	
	N=-18
	S=18
	E=1
	W=-1

	NW=-19
	NE=-17
	SW=17
	SE=19

	def get_surrounding_tiles():
		pass
	

	def G():
		pass
	def H():
		pass
	def F():
		pass
	

	for villan in Villans.List:
		open_list = []
		closed_list = []

		zombie_tile = zombie.get_tile()
		open_list.append(zombie_tile)

		surrounding_nodes = get_surrounding_tiles(zombie_tile)
		





