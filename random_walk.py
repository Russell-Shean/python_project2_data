# random_walk.py

from random import choice

class RandomWalk:
	"""A class to generate random walks"""

	def __init__(self, num_points = 5000):
		"""Initililize the starting values of a random walk"""
		self.num_points = num_points

		# all walks start at the origin
		self.x_values = [0]
		self.y_values = [0]
		self.random_color = ["orange"]


	def fill_walk(self):
		"""fill in the subsequent values of the random walk"""

		# keep making random decisions until n of steps == num_points
		while len(self.x_values) < self.num_points:

			# choose a random direction and random distance to travel
			x_direction = choice([1, -1])
			x_distance = choice(range(1,5))
			x_step = x_direction * x_distance

			y_direction = choice([1, -1])
			y_distance = choice(range(1,5))
			y_step = y_direction * y_distance


			# choose a random color

			random_color = choice(["purple","red","green","blue","orange","yellow"])

			# try again if movement == 0
			if x_step == 0 and y_step ==0:
				continue

			# assuming movement wasn't 0, figure out the new position of the random walk
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step


			# add new location to list
			self.x_values.append(x)
			self.y_values.append(y)
			self.random_color.append(random_color)

