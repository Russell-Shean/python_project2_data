# mpl_squares.py

import matplotlib.pyplot as plt 


# create data

# y axis
squares = []

for value in range(1,6):
	square = value ** 2
	squares.append(square)


# x axis

input_values = []

for value in range(1,6):
	input_values.append(value)


# create plot

# define style
plt.style.use("ggplot")

# define overall plot
fig, ax = plt.subplots()

# specifiy first layer
ax.plot(input_values, squares, linewidth = 3)

# set chart title and labels
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize =14, color = "green")

# set size of tick labels.
ax.tick_params(axis = "both", labelsize = 14)


plt.show()