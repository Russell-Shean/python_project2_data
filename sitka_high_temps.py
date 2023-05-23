# sitka_high_temps.py

import csv
import requests

# download data from github
url = "https://raw.githubusercontent.com/ehmatthes/pcc_3e/main/chapter_16/the_csv_file_format/weather_data/sitka_weather_07-2021_simple.csv"

# download the data
r = requests.get(url, allow_redirects = True)

file_name = 'sitka_weather_07-2021_simple.csv'

open(file_name, 'wb').write(r.content)

with open(file_name) as file:
	reader = csv.reader(file)
	header_row = next(reader)
	print(header_row)