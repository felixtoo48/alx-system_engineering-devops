#!/usr/bin/python3
"""queries reddit api and prints"""

import requests
import sys


def top_ten(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Your User-Agent Here'}

    # Construct the API URL for the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False,
                                params=parameters)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            if len(posts) == 0:
                print(f"No hot posts found in '{subreddit}'.")
            else:
                print(f"Top 10 hot posts in '{subreddit}':")
                for i, post in enumerate(posts, start=1):
                    title = post['data']['title']
                    print(f"{i}. {title}")

        else:
            print("None")

    except Exception as e:
        print(f"An error occurred: {e}")
