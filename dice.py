# dice.py

from random import randint as randomint


class Dice:
	"""Roll the dice if you're feeling lucky"""

	def __init__(self, number_of_sides = 6):
		"""the number of dice faces"""

		self.number_of_sides = number_of_sides

	def roll_dice(self):
		"""Return a random number between 1 and number of sides"""
		return randomint(1, self.number_of_sides)