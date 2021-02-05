#!/usr/bin/python3
"""Module to use the 'Reddit API'"""
import requests


def top_ten(subreddit):
    """Fetch the first 10 hot post listed for
    a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'MyBot/0.0.1'})
    if response.status_code == 200:
        hot = response.json()['data']['children']
        for post in hot[:10]:
            print(post['data']['title'])
    else:
        print(None)
