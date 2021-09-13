
class GameStats: 
	""" Track statistics for alien Invasion """

	def __init__(self, ai_game):
		""" Initialize statistics """
		self.settings = ai_game.settings
		self.reset_stats()

		# Start Alien invasion in an active state
		self.game_active = True

	def reset_stats(self):
		""" Initialize statistics that can change during the game. """
		self.rockets_left = self.settings.rocket_limit
