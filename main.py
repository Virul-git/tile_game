import pygame 
from tileC import Tile
import my_text
import characters
import user_input
from a_star import *


display_width = 800
display_height = 600
	
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)

pygame.init()

############ tiles where the player doesn't step #############
walls = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 21, 41, 61, 81, 101, 121, 141, 161, 181, 201, 221, 241, 261)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tile Game")

for y in range(0,display_height,40):
	for x in range(0,display_width,40):
		if Tile.total_tiles in walls:
			Tile(x,y,'filled')
		else:
			Tile(x,y,'empty')

			

def main():
	clock = pygame.time.Clock()
	FPS = 20
	total_frames = 0

	gameRunning = True
################ initalize villans and Hero ############

	villans = characters.Villans(160,160)
	Hero = characters.Survivor(360,200)

	while True:
		gameDisplay.fill(black)
		a_star(gameDisplay,Hero,total_frames,FPS)
		user_input.get_input(gameDisplay,Hero)
		Tile.draw_tiles(gameDisplay)
		villans.draw_villans(villans,gameDisplay)
		Hero.draw_survivor(gameDisplay)
		my_text.text_display(gameDisplay,"this is to be displayed",50,50)
		pygame.display.update()				
		clock.tick(FPS)
		total_frames +=1
	

if __name__ == "__main__":
	main()
