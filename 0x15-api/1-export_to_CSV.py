#!/usr/bin/python3
"""Using REST API to get information about an employee in CVS format"""
if __name__ == '__main__':

    import requests
    import sys
    import csv

    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(sys.argv[1]))
    req = req.json()
    user = req.get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as f:
        csv = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            if task.get("userId") == int(sys.argv[1]):
                write = [sys.argv[1], user, task.get("completed"),
                         task.get("title")]
                csv.writerow(write)
