"""
   Displays the APRS monitor on a pygame screen
"""

import pygame

from constants import WHITE,BLACK
from controller import Controller

SIZE = (320,240)

def main():
	pygame.init()
	screen = pygame.display.set_mode(SIZE)
	pygame.display.set_caption('APRS')
	done = False
	clock = pygame.time.Clock()
	controller = Controller(SIZE)

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done=True
		screen.fill(WHITE)
		controller.draw(screen)

		pygame.display.flip()
		
		clock.tick(60)
	pygame.quit()

if __name__=='__main__':
	main()
