# sitka_high_temps.py

import csv
import requests
import matplotlib.pyplot as plt 
from datetime import datetime as datetime



# download data from github
url = "https://raw.githubusercontent.com/ehmatthes/pcc_3e/main/chapter_16/the_csv_file_format/weather_data/sitka_weather_2021_simple.csv"

# download the data
r = requests.get(url, allow_redirects = True)

file_name = 'sitka_weather_07-2021_simple.csv'

open(file_name, 'wb').write(r.content)

with open(file_name) as file:
	reader = csv.reader(file)
	header_row = next(reader)
	print(header_row)


	


	for index, column_header in enumerate(header_row):
		print(index, column_header)



	print(list(enumerate(header_row)))


	# extract high temps
	dates, high_temps, low_temps = [], [], []

	for row in reader:
		print(row)
		high = int(row[4])
		high_temps.append(high)

		date = datetime.strptime(row[2], "%Y-%m-%d")
		dates.append(date)

		low = int(row[5])
		low_temps.append(low)



	print(high_temps)

	#for date in dates:
	#	print(date)

	#for row in reader:
	for row in reader:
		print(row)
		

temperature_difference = []

for i in range(0, len(high_temps)):
	temp_diff = high_temps[i] - low_temps[i]
	temperature_difference.append(temp_diff)

print(temperature_difference)


# plot the high temps
plt.style.use("seaborn")

#specify base layer
fig, ax = plt.subplots()

# make the plot
ax.plot(dates, high_temps, color = "red", alpha = 0.5) # orange
#ax.scatter(dates, high_temps, c = "red", s = 20)

ax.plot(dates, low_temps, color = "blue", alpha = 0.5) # purple
#ax.scatter(dates, low_temps, c = "blue", s = 20)

ax.fill_between(dates, high_temps, low_temps, facecolor = "blue", alpha = 0.1)

#ax.plot(dates, temperature_difference, c = "yellow")
#ax.scatter(dates, temperature_difference, c = "green", s = 20)

ax.set_title("Daily Maximum temperatures 2018 in Sitka, Alaska", fontsize = 20)
ax.set_xlabel("", fontsize = 16)
fig.autofmt_xdate()

ax.set_ylabel("Daily maximum temperature (F)", fontsize = 16)

#ax.tick_params(axis = "y", which = "major", labelsize = 16 )
ax.tick_params(axis = "both", which = "minor", labelsize = 40, labelcolor = "green" )

plt.show()



cats = ["kitty", "whiskers", "Mr. Fluffles"]

enumerate(cats)