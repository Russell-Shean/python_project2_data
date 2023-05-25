# time_abroad.py

import matplotlib.pyplot as plt 
import csv
import pandas

# load data

file_name = "/home/russ/Documents/r_projects/time_abroad/foreign_travel.csv"

with open(file_name) as file:
	reader = csv.reader(file)
	column_headings = next(reader)

	print(list(reader))
	print(column_headings)



countries_df = pandas.read_csv(file_name)


#print(countries_df)


# make a matplotlib plot

# specify default style
plt.style.use("seaborn")

# specify context

fig, ax = plt.subplots()


ax.bar(countries_df["country"], countries_df["number_of_days"])

ax.set_xlabel("Country")
ax.set_ylabel("Number of Days")

#plt.show()