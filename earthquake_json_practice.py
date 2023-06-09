# earthquake_json_practice

# load external libraries
import requests
import json

# define url
url = "https://raw.githubusercontent.com/ehmatthes/pcc_3e/main/chapter_16/mapping_global_datasets/eq_data/eq_data_1_day_m1.geojson"

# define new file name
file_name = "one_day_earthquaqes.geojson"
readable_file_name = "readable_earthquakes.geojson"

# use the requests package to download the file
requested_file = requests.get(url, allow_redirects = True)

# unreadable -------------------------------------------------
# open the file we want to write to 
# then write the download content to that file

open(file_name, "wb").\
write(requested_file.content)



# open the newly saved file
with open(file_name) as file:
	earthquake_data = json.load(file)



# dump the new file to a new new file with indents
with open(readable_file_name, "w") as file:
	json.dump(earthquake_data, file, indent = 4)


all_earthquakes = earthquake_data["features"]

print(len(all_earthquakes))



magnitudes, longitudes, latitudes = [], [], []

for earthquake in all_earthquakes:
	magnitude = earthquake["properties"]["mag"]
	longitude = earthquake["geometry"]["coordinates"][0]
	latitude = earthquake["geometry"]["coordinates"][1]
	magnitudes.append(magnitude)
	longitudes.append(longitude)
	latitudes.append(latitude)

print(magnitudes[:10])
print(latitudes[:10])
print(longitudes[:10])