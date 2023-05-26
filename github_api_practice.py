# github_api_practice.py

import requests

# define the API call
url = 'https://api.github.com/search/repositories?q=language:R&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers = headers)

print(f"Status code: {r.status_code}")

#store the API reponse in a dictionary
response_dictionary = r.json()

# Print the dictionary keys from the returned results
print(response_dictionary.keys())