# mpl_squares.py

import matplotlib.pyplot as plt 

squares = []

for value in range(1,6):
	square = value ** 2
	squares.append(square)

print(squares)


fig, ax = plt.subplots()

ax.plot(squares)


plt.show()