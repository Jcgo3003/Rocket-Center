import sys
import pygame
from settings import Settings
from rocket import Rocket 

class RocketCenter:
	""" A class to manage the general game assets and behavior """

	def __init__(self):
		""" Initialize the game, and create game resources """
		pygame.init()
		
		# Getting all the settings
		self.settings = Settings()

		# Setting fullscreen mode
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) 
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		# Getting a name for the title
		pygame.display.set_caption("Rocket Center")

		# Setting my rocket 
		self.rocket = Rocket(self)

	def run_game(self):
		""" Start the main loop for the game """
		while True:
			# Setting the check_events, update_screen and rocket update methons"""
			self._check_events()
			self._update_screen()
			self.rocket.update()

	def _check_events(self):
		""" Reponding te keypresses """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		""" Respond to keypresses """
		if event.key == pygame.K_RIGHT:
			self.rocket.moving_right = True

		elif event.key == pygame.K_LEFT:
			self.rocket.moving_left = True

		elif event.key == pygame.K_UP:
			self.rocket.moving_up = True

		elif event.key == pygame.K_DOWN:
			self.rocket.moving_down = True

		elif event.key == pygame.K_q:
			sys.exit()


	def _check_keyup_events(self, event):
		""" Respond to keyup """
		if event.key == pygame.K_RIGHT:
			self.rocket.moving_right = False
		
		elif event.key == pygame.K_LEFT:
			self.rocket.moving_left = False

		elif event.key == pygame.K_UP:
			self.rocket.moving_up = False

		elif event.key == pygame.K_DOWN:
			self.rocket.moving_down = False
		
		


	def _update_screen(self):
		""" Updating all the images in the screen """
		self.screen.fill(self.settings.bg_color)
		self.rocket.blitme()
		pygame.display.flip()

if __name__ == "__main__":
	param = RocketCenter()
	param.run_game()





