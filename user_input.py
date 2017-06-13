import pygame
from tileC import Tile

def get_input(gameDisplay,Hero):

	Mpos = pygame.mouse.get_pos()
	Mx = Mpos[0]/Tile.width
	My = Mpos[1]/Tile.height
	Mnum = (Mx+1)+(My*18)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		print event
		if event.type == pygame.MOUSEBUTTONDOWN:
			A =Tile.get_tile(Mnum)
			A.type = 'filled'
			A.walkable = False
			if pygame.event.key == pygame.M_1:
				print "button 1 pressed"
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				future_tile = Hero.get_number()-Tile.V
				if Tile.get_tile(future_tile).walkable:
					print future_tile
					Hero.y -= Tile.height
			if event.key == pygame.K_s:
				future_tile = Hero.get_number()+Tile.V
				if Tile.get_tile(future_tile).walkable:
					print future_tile
					Hero.y += Tile.height
			if event.key == pygame.K_a:
				future_tile = Hero.get_number()-Tile.H
				if Tile.get_tile(future_tile).walkable:
					print future_tile
					Hero.x -= Tile.width
			if event.key == pygame.K_d:
				future_tile = Hero.get_number()+Tile.H
				if Tile.get_tile(future_tile).walkable:
					print future_tile
					Hero.x += Tile.width
				
