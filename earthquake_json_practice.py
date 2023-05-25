# earthquake_json_practice

# load external libraries
import requests 

# define url
url = "https://raw.githubusercontent.com/ehmatthes/pcc_3e/main/chapter_16/mapping_global_datasets/eq_data/eq_data_1_day_m1.geojson"

# define new file name
file_name = "one_day_earthquaqes.geojson"

# use the requests package to download the file
requested_file = requests.get(url, allow_redirects = True)

open(file_name, "wb").write(requested_file.content)