
class Settings:
	""" A class to store all the settings for rocket center game """

	def __init__(self):
		# Getting the screen size 
		self.screen_width = 1200
		self.screen_height = 800
		
		# Setting the background color
		self.bg_color = (66, 95, 192)

		# Rocket settings
		self.rocket_speed = 20