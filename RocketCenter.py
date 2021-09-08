""" Third version of Rocket center  vertical movement """
# In this version is added:
# A fleet of aliens comming towards the ship and dissapear if hit by a bullet

import sys
import pygame
from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien
import random

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
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def _create_fleet(self):
		""" Creating a fleet of aliens """
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size

		# Available space in x
		rocket_width = self.rocket.rect.width 
		available_space_x = self.settings.screen_width - (3 * alien_width) - rocket_width
		number_columns = available_space_x // (2 * alien_width)

		star_point_x = self.settings.screen_width - available_space_x

		# Available space in y
		available_space_y = self.settings.screen_height
		number_aliens = available_space_y // (2 * alien_height)


		for number_alien in range(number_aliens):
			for number_column in range(number_columns):
			# Creating an alien and place it in row,and saving 
				r = random.randint(0, 50)

				if not(r % 2):
					self._create_alien(number_column,number_alien, star_point_x)


	def _create_alien(self, number_column, number_alien, star_point_x):
		""" Creating an alien """
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		
		alien.x = alien_width + star_point_x + (2 * alien_width * number_column)

		alien.rect.x = alien.x 
		alien.rect.y = alien.rect.height + (2 * alien.rect.height * number_alien)

		self.aliens.add(alien)

		return [alien.rect.x, alien.rect.y]


	def _check_fleet_edges(self):
		""" Respond apprepriately if any aliens have reache an edge """
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		""" Get the enitre fleet to the left"""
		for alien in self.aliens.sprites():
			alien.rect.x += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= 1

	def run_game(self):
		""" Start the main loop for the game """
		while True:
			# Setting the check_events, update_screen and rocket update methons"""
			self._check_events()
			self._update_screen()
			
			self.rocket.update()
			self._update_bullets()

			self._update_aliens()


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
		if event.key == pygame.K_UP:
			self.rocket.moving_up = True

		elif event.key == pygame.K_DOWN:
			self.rocket.moving_down = True

		elif event.key == pygame.K_q:
			sys.exit()

		elif event.key == pygame.K_SPACE:
			self._fire_bullet()


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
		
	def _fire_bullet(self):
		""" Create a new bullet and add ti to the bullet group """
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self): 
		""" Update the position of bullets and get gir of old ones """
		self.bullets.update()

		# Get rid of the bullets that have disappeared.
		for bullet in self.bullets.copy():
			if bullet.rect.left >= self.settings.screen_width:
				self.bullets.remove(bullet)

		self._check_bullet_alien_collisions()


	def _check_bullet_alien_collisions(self):
		""" Respond to bullet-alien collisions."""
		# Remove any bullets and aliens that have collide
		collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

		# Check for empty groups and creating a new fleet
		if not self.aliens:
			# Destroy exitsting bullets and create new fleet.
			self.bullets.empty()
			self._create_fleet()
			
	def _update_aliens(self):
		""" Check if the fleet is at an edge,
		then update the possitions of all arliens in the fleet."""
		self._check_fleet_edges()
		self.aliens.update()

	def _update_screen(self):
		""" Updating all the images in the screen """
		self.screen.fill(self.settings.bg_color)
		self.rocket.blitme()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		self.aliens.draw(self.screen)

		pygame.display.flip()

if __name__ == "__main__":
	param = RocketCenter()
	param.run_game()





