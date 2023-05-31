# repo_stars_barchart.py

import requests

from plotly.graph_objs import Bar
from plotly import offline

#define URL and API call
url = 'https://api.github.com/search/repositories?q=language:R&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

# make API call
r = requests.get(url, headers = headers)
print(f"Status code: {r.status_code}")

# save as dictionary
response_dictionary = r.json()
returned_repos = response_dictionary['items']

# pull important results
repo_links, stars, labels = [], [], []

for repo in returned_repos:
	# repo_names.append(repo['name'])
	stars.append(repo['stargazers_count'])

	owner = repo['owner']['login']
	description = repo['description']
	label = f"{owner}</br>{description}"
	labels.append(label)

	repo_name = repo['name']
	repo_url = repo['html_url']
	repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
	repo_links.append(repo_link)


# make the plotly chart
data = [{
	'type':'bar',
	'x':repo_links,
	'y':stars,
	'hovertext': labels,
	'marker': {
		'color': 'rgb(60, 100, 150)',
		'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
	},
	'opacity': 0.8
}]



chart_layout = {
	'title': "Most starred R repositories on Github",
	'titlefont': {'color': "purple", 'size': 28},
	'xaxis': { 'title': 'Repository',
	           'titlefont':{'size': 24},
	           'tickfont': {'size': 14, 'color': "green"}},
	'yaxis': { 'title': 'Number of Stars',
	           'titlefont': {'size':24},
	           'tickfont': {'size': 14}}
}


fig = {'data':data, 'layout':chart_layout}

offline.plot(fig, filename = 'starred_R_repos.html')