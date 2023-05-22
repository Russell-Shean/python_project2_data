# scatter_squares.py

import matplotlib.pyplot as plt 


# define data
x_values = range(1,1001)
y_values = [x**2 for x in x_values]


plt.style.use("seaborn")

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s = 10, c = y_values, cmap = plt.cm.Blues)

# set chart title and label axes
ax.set_title("Square numbers", fontsize = 24, color = "purple")
ax.set_xlabel("Value", fontsize = 12)
ax.set_ylabel("Square", fontsize = 20, color = (0, 0.9, 0))


# set ticks
ax.tick_params(axis = "both", which = "major", labelsize = 14)

# set axis range
ax.axis([0,1100,0,1100000])


# show the plot
# plt.show()

# save the plot
plt.savefig("square_plot.png", bbox_inches = "tight")