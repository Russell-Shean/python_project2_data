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


# Start looking at the dictionary of results
print(f"Total number of repositories: {response_dictionary['total_count']}")


# find sub dictionaries
repo_dictionaries = response_dictionary["items"]

# number of repos returned
print(f"Number of repos returned: {len(repo_dictionaries)}")


# look at the first repository
repo_0 = repo_dictionaries[0]

print(f"Number of items: {len(repo_0)}")

for key in sorted(repo_0.keys()):
	print(key)


for i in range(len(repo_dictionaries)):
	print(f"{repo_dictionaries[i]['name']}: {repo_dictionaries[i]['description']}")


print("\nInfo about the first repo!")
print(f"Name: {repo_0['name']}")
print(f"Owner: {repo_0['owner']['login']}")
print(f"Stars: {repo_0['stargazers_count']}")
print(f"Repository Link: {repo_0['html_url']}")
print(f"Create Date: {repo_0['created_at']}")
print(f"Update Date: {repo_0['updated_at']}")
print(f"Description: {repo_0['description']}")


print("\nSummary Info about all the Repos!")
for repo in repo_dictionaries:
	print(f"Name: {repo['name']}")
	print(f"Owner: {repo['owner']['login']}")
	print(f"Stars: {repo['stargazers_count']}")
	print(f"Repository Link: {repo['html_url']}")
	print(f"Description: {repo['description']}\n")