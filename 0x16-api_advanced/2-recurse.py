#!/usr/bin/python3
"""Using the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Fetches all the titles of hot section
    of a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(subreddit,
                                                                  after)
    response = requests.get(url, headers={'User-Agent': 'MyBot/0.0.1'})
    if response.status_code == 200:
        after = response.json()['data']['after']
        for data in response.json()['data']['children']:
            hot_list.append(data['data']['title'])
        if after:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None
