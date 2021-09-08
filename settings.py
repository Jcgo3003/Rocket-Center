
class Settings:
	""" A class to store all the settings for rocket center game """

	def __init__(self):
		# Getting the screen size 
		self.screen_width = 1200
		self.screen_height = 800
		
		# Setting the background color
		self.bg_color = (66, 95, 192)

		# Rocket settings
		self.rocket_speed = 8

		# Bullet settings
		self.bullet_speed = 16.0
		self.bullet_width = 15
		self.bullet_height = 4
		self.bullet_color = (255, 255, 255)
		self.bullets_allowed = 6

		# Alien settings 
		self.alien_speed = 0.1


		# Fleet_direction will always move left
		self.fleet_direction = -1

		
