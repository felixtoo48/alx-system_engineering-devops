#!/usr/bin/python3
"""Function to count words """""

import requests
import sys


def count_words(subreddit, word_list, after=None, word_count=None):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Your User-Agent Here'}

    if word_count is None:
        word_count = {}

    # Construct the API URL for the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            if len(posts) == 0:
                sorted_results = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_results:
                    print(f"{word}: {count}")
                return

            for post in posts:
                title = post['data']['title']
                words = title.lower().split()

                for word in word_list:
                    if word in words:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1

            # Check if there are more pages to fetch
            after = data['data']['after']
            return count_words(subreddit, word_list, after, word_count)

        else:
            print("Invalid subreddit.")
            return

    except Exception as e:
        print(f"An error occurred: {e}")
        return
