#!/usr/bin/python3
"""100-count"""

import requests
import sys
import json


def count_languages_recursive(data, language_counts):
    if isinstance(data, dict):
        if "title" in data.get("data", {}):
            title = data["data"]["title"].lower()
            for language in language_counts:
                if language in title:
                    language_counts[language] += 1
        for key, value in data.items():
            count_languages_recursive(value, language_counts)
    elif isinstance(data, list):
        for item in data:
            count_languages_recursive(item, language_counts)


def count_words(subreddit, word_list, after=None, word_count=None):
    if word_count is None:
        word_count = {}

    headers = {'User-Agent': 'Your User-Agent Here'}
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

            after = data['data']['after']
            return count_words(subreddit, word_list, after, word_count)

        # Sample JSON data containing Reddit post information
        reddit_posts = [print(response.content)]

        # Dictionary to store programming language counts
        programming_languages = {
                "java": 0,
                "javascript": 0,
                "python": 0,
                "react": 0,
                "scala": 0
            }

        # Count programming languages recursively
        count_languages_recursive(reddit_posts, programming_languages)

        # Print the programming language counts
        for language, count in programming_languages.items():
            print(f"{language}: {count}")
        
        else:
            return


    except Exception as e:
        print(f"An error occurred: {e}")
        return
