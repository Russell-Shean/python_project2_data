# dice_chart.py

from plotly.graph_objs import Bar, Layout
from plotly import offline

from dice import Dice 

# create a dice instance

dice = Dice()


# store 100 rolls of the dice in a list

dice_rolls = []

for i in range(1000):
	dice_rolls.append(dice.roll_dice())


# count frequency of different dice rolls

frequencies = []

for number in range(1, dice.number_of_sides + 1):
	frequency = dice_rolls.count(number)
	frequencies.append(frequency)



print(frequencies)


# make a plotly histogram
x_values = list(range(1, dice.number_of_sides + 1))
dice_rolls_freq_df = [Bar(x = x_values, y = frequencies)]

x_axis_aes = {"title":"Value of Dice Roll"}
y_axis_aes = {"title": "Frequency"}

plot_layout = Layout(title = "Frequency by value for 1000 rolls of a 6 sided dice",
	                 xaxis = x_axis_aes,
	                 yaxis = y_axis_aes)

offline.plot({"data": dice_rolls_freq_df,
	          "layout": plot_layout},
	          filename = "1000_dice_rolls.html")

