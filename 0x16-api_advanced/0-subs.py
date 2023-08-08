#!/usr/bin/python3
"""query reddit api"""
import requests

proxies = {
    'http': 'http://your_proxy_here',
    'https': 'http://your_proxy_here'
}

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'Your User-Agent Here'}

    # Construct the API URL for the subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Test the function
subreddit_name = 'programming'
subscribers_count = number_of_subscribers(subreddit_name)
print(f"Subscribers in '{subreddit_name}': {subscribers_count}")
