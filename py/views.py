"""
    Manages displaying the data model in various ways
"""
import pygame

from constants import BLACK,X,Y

def draw_text_at(screen, text, x, y, font_size=30, bold=False,italic=False):
	font = pygame.font.SysFont(None, font_size, bold, italic)
	text = font.render(text,True,BLACK)
	textpos = text.get_rect()
	screen.blit(text,(x,y))
	return y + textpos.height

def draw_centered_text(screen, text, x, y, right,font_size=30,bold=True,italic=False):
	# Draw centered text at the given x and y, with the provided font size,
	# and return the y coordinate of the bottom of the text
	font = pygame.font.SysFont(None, font_size, bold, italic)
	text = font.render(text,True,BLACK)
	textpos = text.get_rect()
	text_left = x + ((right - x - textpos.width) / 2)
	screen.blit(text,(text_left,y))
	return y + textpos.height


class ClockView(object):
	def draw(self,screen,top_left,bottom_right, top_offset):
		# Draw current time
		draw_centered_text(screen,"14:23:00",top_left[X],top_offset,bottom_right[X])

class WeatherView(object):
	def draw(self,screen,top_left,bottom_right, top_offset):
		last_y = draw_centered_text(screen,"25F",top_left[X],top_left[Y]+top_offset,bottom_right[X])
		draw_centered_text(screen,"KC2ZUF, 12 km", top_left[X], last_y+5,bottom_right[X],font_size=15)

class BeaconView(object):
	def draw(self,screen,top_left,bottom_right, top_offset):
		last_y = draw_centered_text(screen,"KC2ZUF-7",top_left[X],top_left[Y]+top_offset,bottom_right[X])
		draw_centered_text(screen,"45.34W, 41.24N", top_left[X], last_y+5,bottom_right[X],font_size=20)

class BeaconControlView(object):
	def draw(self,screen,top_left,bottom_right, top_offset):
		draw_centered_text(screen,"Beacon ON",top_left[X],top_left[Y]+top_offset, bottom_right[X],
				font_size=20,bold=False,italic=True)

class CompassView(object):
	COMPASS_MARGIN_Y = 20
	COMPASS_MARGIN_X = 10 
	COMPASS_R1 = 20
	COMPASS_R2 = 50
	COMPASS_R3 = 80

	def draw(self,screen,top_left,bottom_right, top_offset):
		center_x = bottom_right[X] / 2
		center_y = bottom_right[Y] / 2
		
		draw_text_at(screen,"N", center_x-3,4,font_size=15,bold=False)
		pygame.draw.line(screen, BLACK, (center_x, CompassView.COMPASS_MARGIN_Y), 
						(center_x, bottom_right[Y]-CompassView.COMPASS_MARGIN_Y))
		pygame.draw.line(screen, BLACK, (CompassView.COMPASS_MARGIN_X, center_y), 
						(bottom_right[X]-CompassView.COMPASS_MARGIN_X, center_y))
		pygame.draw.circle(screen, BLACK, (center_x,center_y), CompassView.COMPASS_R1,1)
		pygame.draw.circle(screen, BLACK, (center_x,center_y), CompassView.COMPASS_R2,1)
		pygame.draw.circle(screen, BLACK, (center_x,center_y), CompassView.COMPASS_R3,1)



