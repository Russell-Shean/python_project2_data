# hacker_news_API.py

import requests
import json

# define API call
url = "https://hacker-news.firebaseio.com/v0/item/19155826.json"

r = requests.get(url)
print(f"Status Code:{r.status_code}")

results_dict = r.json()
readable_file = "readable_hacker_news.json"

with open(readable_file, 'w') as f:
	json.dump(results_dict, f, indent = 4)