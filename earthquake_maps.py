# earthquake_maps.py

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import requests


# define url
url = "https://raw.githubusercontent.com/ehmatthes/pcc_3e/main/chapter_16/mapping_global_datasets/eq_data/eq_data_30_day_m1.geojson"

# define new file name
file_name = "30_day_earthquaqes.geojson"
readable_file_name = "readable_30_earthquakes.geojson"

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



magnitudes, longitudes, latitudes, hover_text = [], [], [], []

for earthquake in all_earthquakes:
	magnitude = earthquake["properties"]["mag"]
	longitude = earthquake["geometry"]["coordinates"][0]
	latitude = earthquake["geometry"]["coordinates"][1]
	hover_title = earthquake["properties"]['title']

	magnitudes.append(magnitude)
	longitudes.append(longitude)
	latitudes.append(latitude)
	hover_text.append(hover_title)


data = [{
         'type': 'scattergeo',
         'lon' : longitudes, 
         'lat' : latitudes,
         'text': hover_text,
         'marker': {
              'size': [7.5 * mag for mag in magnitudes],
              'color': magnitudes,
              'colorscale': 'Viridis',
              'reversescale': True,
              'colorbar': {'title': 'Magnitude'}
         },
         }]





my_layout = Layout(title = "Earthquakes by magnitude")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = "global_earthquakes.html")