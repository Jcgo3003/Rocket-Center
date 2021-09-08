import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
	""" A class to  represen a single alien """
	
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen

		# Settings 
		self.settings = ai_game.settings

		# Load the alien image and set its rect attribute
		self.image = pygame.image.load("images/spaceship.bmp")
		self.rect = self.image.get_rect()

		# Store the alien's position 
		self.x = float(self.rect.x)

	def update(self):
		""" Move the alien towards the rocket """
		self.x += (self.settings.alien_speed * self.settings.fleet_direction)
		self.rect.x = self.x 

	def check_edges(self):
		""" Return True if the alien is too close to the left screen """
		screen_rect = self.screen.get_rect

		if self.rect.left <= 0:
			return True





