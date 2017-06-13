import pygame 
from tileC import Tile

display_width = 720
display_height = 440
	
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)

pygame.init()

############ tiles where the player doesn't step #############
walls = (1,2,3,4,5,6,7,8,9,10)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tile Game")

clock = pygame.time.Clock()
FPS = 24
total_frames = 0

for y in range(0,display_height,40):
	for x in range(0,display_width,40):
		if Tile.total_tiles in walls:
			Tile(x,y,'filled')
		else:
			Tile(x,y,'empty')



def main():
	gameRunning = True
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					pygame.quit()
					quit()
		Tile.draw_tiles(gameDisplay)
		pygame.display.update()				
	

if __name__ == "__main__":
	main()
