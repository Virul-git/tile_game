import pygame
from characters import *
from tileC import Tile


def a_star(gameDisplay,Hero,total_frames,FPS):
	
	N=-20
	S=20
	E=1
	W=-1

	NW=-21
	NE=-19
	SW=19
	SE=21


	for tile in Tile.List:
		tile.parent = None
		tile.H, tile.G, tile.F = 0,0,0

	def blocky(tiles,diagonals,surrounding_node):
		if surrounding_node.number not in diagonals:
			tiles.append(surrounding_node)
		return tiles

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

		onn = base_node.number
		diagonals = [onn+NE,onn+SW,onn+NW,onn+SE]

		for tile_number in array:

			surrounding_tile = Tile.get_tile(tile_number)
			if tile_number not in range(1, Tile.total_tiles+1):
				continue
			if (surrounding_tile.walkable and surrounding_tile not in closed_list):
				#tiles.append(surrounding_tile) diagonal movenent
				tiles = blocky(tiles,diagonals,surrounding_tile)

		return tiles

	def G(tile):
		
		diff = tile.number - tile.parent.number

		if diff in (N, S, E, W):
			tile.G = tile.parent.G +10
		elif diff in (NW, NE, SW, SE):
			tile.G = tile.parent.G +14



	def H():
		for tile in Tile.List:
			tile.H = 10*(abs(tile.x-Hero.x) +abs(tile.y-Hero.y))/ Tile.width


	def F(tile):
		tile.F = tile.G + tile.H
	
	def swap_tile(tile):
		open_list.remove(tile)
		closed_list.append(tile)


	def get_LFT():

		lft = []

		for tile in open_list:
			lft.append(tile.F)

		o = open_list[::-1]

		for tile in o:
			if tile.F == min(lft):
				return tile

	def mov_G_cost(LFT, node):
		Gval =0
		diff = LFT.number - node.number

		if diff in (N, S, E, W):
			Gval = LFT.G+10
		elif diff in (NW, NE, SW, SE):
			Gval = LFT.G+14

		return Gval



	def loop():

		LFT = get_LFT()

		swap_tile(LFT)

		surrounding_nodes = get_surrounding_tiles(LFT)

		for node in surrounding_nodes:
			if node not in open_list:
				open_list.append(node)
				node.parent = LFT

			elif node in open_list:
				calc_G = mov_G_cost(LFT, node)
				if calc_G < node.G:
					node.parent = LFT
					G(node)
					F(node)


		if open_list == [] or Hero.get_tile() in closed_list:
			return
		for node in open_list:
			G(node)
			F(node)

			half = Tile.width/2
		#	pygame.draw.line(gameDisplay,[255,0,0],[node.parent.x+half,node.parent.y+half],[node.x+half,node.y+half])

		loop()


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

		for node in surrounding_nodes:
			G(node)
			F(node)

		loop()

		return_tiles = []

		parent = Hero.get_tile()

		while True:

			return_tiles.append(parent)

			parent = parent.parent

			if parent == None:
				break
			if parent.number == villan.get_number():
				break


		half = Tile.width/2

		for tile in return_tiles:
			pygame.draw.circle(gameDisplay,[10,250,50],[tile.x+half,tile.y+half],half/4)
			

		if len(return_tiles)>1:
			if total_frames % (FPS/2) == 0:
				next_tile = return_tiles[-1]
				villan.x = next_tile.x
				villan.y = next_tile.y



