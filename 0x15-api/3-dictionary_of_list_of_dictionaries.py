#!/usr/bin/python3
"""Get a lis of list of all employees"""
if __name__ == "__main__":

    import json
    import requests
    import sys

    req = requests.get('https://jsonplaceholder.typicode.com/users/')
    req = req.json()
    ids = {}
    for user in req:
        ids[user.get("id")] = user.get("username")
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    dic = {}
    for task in todos:
        user_id = task.get("userId")
        username = ids[user_id]
        t = task.get("title")
        completed = task.get("completed")
        d = {"username": username, "task": t, "completed": completed}
        if dic.get(user_id):
            dic.get(user_id).append(d)
        else:
            dic[user_id] = [d]

    with open('todo_all_employees.json', 'w', newline='') as f:
        json.dump(dic, f)
