#!/usr/bin/python3
"""recursive function that querries reddit api"""

import requests
import sys


def recurse(subreddit, hot_list=None, after=None):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Your User-Agent Here'}

    if hot_list is None:
        hot_list = []

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
                return hot_list

            for post in posts:
                title = post['data']['title']
                hot_list.append(title)

            # Check if there are more pages to fetch
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list

            if hot_list:
                print(f"Hot articles in '{subreddit}':")
                for i, title in enumerate(hot_articles, start=1):
                    print(f"{i}. {title}")
            else:
                print(f"No hot articles found in '{subreddit}'.")

        else:
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
