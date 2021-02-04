#!/usr/bin/python3
"""Module to use the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Fetch the amount of
    suscribers of a subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'MyBot/0.0.1'})
    if response.status_code == 200:
        subs = response.json()['data']['subscribers']
        return subs
    return 0