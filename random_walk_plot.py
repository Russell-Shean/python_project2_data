# random_walk_plot.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# make a random walk using an instance of the RandomWalk class

random_walk = RandomWalk(50_000)

random_walk.fill_walk()


# plot all the points in the random walk

# Define plot style
plt.style.use("classic")

# call base plot
fig, ax = plt.subplots(figsize = (20, 15), dpi = 144)

# number the points in order
point_numbers = range(random_walk.num_points)


# Multi color walk:

# make a scatter plot of the random walk
ax.scatter(random_walk.x_values, random_walk.y_values, 
	#c = random_walk.random_color, 
	c = point_numbers,
	edgecolors = "none",
	s = 1)

# one color in order

#ax.scatter(random_walk.x_values, random_walk.y_values, 
	#c = random_walk.random_color, 
#	c = point_numbers,
#	cmap = plt.cm.Blues,
#	edgecolors = "none",
#	s = 1)


# add a big green dot for the start point
ax.scatter(0, 0, c = "green", edgecolors = "none", s = 100)

# add big red dot for end point
ax.scatter(random_walk.x_values[-1],
	       random_walk.y_values[-1],
	       c = "red",
	       edgecolors = "none",
	       s = 100)



# remove the axis
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()
