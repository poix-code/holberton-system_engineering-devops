#!/usr/bin/python3
"""Using a REST API to get information of an ID employee"""
if __name__ == '__main__':

    import requests
    import sys

    req = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
    req = req.json()
    name = req.get("name")

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    tasks = []
    total = 0
    for task in todos:
        if task.get("userId") == int(sys.argv[1]):
            total += 1
            if task.get("completed") is True:
                tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(tasks),
                                                          total))
    for tab in tasks:
        print("\t {}".format(tab))
