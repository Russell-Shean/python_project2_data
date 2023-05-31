# hacker_news_top_stories.py

import requests

from operator import itemgetter

# make API call and store response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code: {r.status_code}")

# Process each story
story_ids = r.json()
story_dictionaries = []

for id in story_ids[:6]:

	# Make a new API call
	url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
	r2 = requests.get(url)
	print(f"ID: {id}\tStatus Code:{r2.status_code}")

	returned_dictionary = r2.json()


	# build a dictionary for each article
	article_dictionary = {
		'title': returned_dictionary['title'],
		'link': f"http://news.ycombinator.com/item?id={id}",
		'comments': returned_dictionary['descendants'],
	}

	story_dictionaries.append(article_dictionary)


# Vectorized opperation! to pull comments
story_dictionaries = sorted(story_dictionaries, key = itemgetter('comments'), reverse = True)

for story in story_dictionaries:
	print(f"\nTitle: {story['title']}")
	print(f"Link: {story['link']}")
	print(f"Comments: {story['comments']}")


