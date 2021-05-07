import pygame

class Rocket:
	""" A class define and manage the rocket """
	def __init__(self, param_game):
		# Getting the screen parameter from center Rocket
		self.screen = param_game.screen

		# Getting the settings from center Rocket
		self.settings = param_game.settings

		# Getting the rocket on the screen
		self.screen_rect = param_game.screen.get_rect()

		# Loading the image 
		self.image = pygame.image.load("images/bla.bmp")

		# Getting the image
		self.rect = self.image.get_rect()

		# Positioning the image
		self.rect.center = self.screen_rect.center

		# Storing the position of the rocket
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		""" Update the rocket position using all the movement flags """
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.rocket_speed

		if self.moving_left and self.rect.left > 10:
			self.x -= self.settings.rocket_speed

		if self.moving_up and self.rect.top > 10:
			self.y -= self.settings.rocket_speed

		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.rocket_speed

		# Update rect object 
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		""" Drawing the rocket at its current location """
		self.screen.blit(self.image, self.rect)

