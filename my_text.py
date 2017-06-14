import pygame


def text_display(gameDisplay,text,x,y,size=10,color=(255,255,255),font='monospace'):

		try:
			text = str(text)
			font = pygame.font.SysFont(font,size)
			text = font.render(text,True,color)
			gameDisplay.blit(text,(x,y))
		except Exception, e:
			print 'Error importing the given font.'
			raise e
		
