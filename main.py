import pygame 


display_width = 420
display_height = 420
	
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue =(0,0,255)

pygame.init()


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("BOX")


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
		pygame.display.update()				
	

if __name__ == "__main__":
	main()
