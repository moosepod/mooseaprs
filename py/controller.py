""" 
    Handles the logic and state management for the monitor app. 
"""
import pygame

from constants import BLACK,X,Y
from views import ClockView,WeatherView,BeaconView,CompassView,BeaconControlView
SPLIT_X = 320 * 2/3

PANE_2A_TEXT_OFFSET = 20
PANE_2B_TEXT_OFFSET = 10
PANE_2C_TEXT_OFFSET = 20
PANE_2D_TEXT_OFFSET = 13

PANE_2B_Y= 60
PANE_2C_Y = 120
PANE_2D_Y = 200

class Controller(object):
	def __init__(self,size):
		self.size = size
		self.pane_2a = ClockView()
		self.pane_2b = WeatherView()
		self.pane_2c = BeaconView()
		self.pane_2d = BeaconControlView()
		self.pane_1  = CompassView()


	def draw(self,screen):
		# Line splitting the two parts of the screen
		pygame.draw.line(screen,BLACK, (SPLIT_X,0),(SPLIT_X,self.size[X]))
	
		# Line splitting up the three areas on the right pane
		pygame.draw.line(screen,BLACK, (SPLIT_X,PANE_2B_Y), (self.size[X], PANE_2B_Y))
		pygame.draw.line(screen,BLACK, (SPLIT_X,PANE_2C_Y), (self.size[X], PANE_2C_Y))
		pygame.draw.line(screen,BLACK, (SPLIT_X,PANE_2D_Y), (self.size[X], PANE_2D_Y))
	
		self.pane_1.draw(screen,(0,0),(SPLIT_X,self.size[Y]),0)
		self.pane_2a.draw(screen,(SPLIT_X,0),(self.size[X],PANE_2B_Y),PANE_2A_TEXT_OFFSET)
		self.pane_2b.draw(screen,(SPLIT_X,PANE_2B_Y),(self.size[X],PANE_2C_Y), PANE_2B_TEXT_OFFSET)
		self.pane_2c.draw(screen,(SPLIT_X,PANE_2C_Y),(self.size[X],self.size[Y]), PANE_2C_TEXT_OFFSET)
		self.pane_2d.draw(screen,(SPLIT_X,PANE_2D_Y),(self.size[X],self.size[Y]), PANE_2D_TEXT_OFFSET)

