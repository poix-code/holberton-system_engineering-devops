#!/usr/bin/python3
"""Export information about an employee in JSON format"""
if __name__ == '__main__':

    import requests
    import sys
    import json

    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                       format(sys.argv[1]))
    req = req.json()
    user = req.get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    dic = {str(sys.argv[1]): []}
    for task in todos:
        if task.get("userId") == int(sys.argv[1]):
            key = {}
            key["task"] = task.get("title")
            key["completed"] = task.get("completed")
            key["username"] = user
            dic[str(sys.argv[1])].append(key)
    with open('{}.json'.format(sys.argv[1]), 'w', newline='') as f:
        json.dump(dic, f)
