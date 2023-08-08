#!/usr/bin/python3
"""recursive function that queries reddit api"""

import requests
import sys


def count_words(subreddit, word_list, after=None, count_dict=None):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Your User-Agent Here'}

    if count_dict is None:
        count_dict = {}

    # Construct the API URL for the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            if len(posts) == 0:
                return count_dict

            for post in posts:
                title = post['data']['title']
                for word in word_list:
                    word = word.lower()
                    if f" {word.lower()} " in f" {title.lower()} ":
                        count_dict[word] = count_dict.get(word, 0) + 1

            # Check if there are more pages to fetch
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                return count_dict

        else:
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
