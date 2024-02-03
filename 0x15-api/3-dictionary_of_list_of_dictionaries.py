#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries module
For a rest api that fetched employee data
"""
import json
import requests
import sys


def all_users_tasks():
    """Fetches and displays all users tasks
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = "{}/users".format(base_url)

    response = requests.get(users_url)
    users = response.json()
    data = {}
    for user in users:
        user_tasks = []
        user_tasks_url = '{}/{}/todos'.format(users_url, user['id'])
        response = requests.get(user_tasks_url)
        tasks = response.json()
        for task in tasks:
            user_tasks.append({
                'username': user['name'],
                'task': task['title'],
                'completed': task['completed']
            })
        data[str(user['id'])] = user_tasks

    file_name = 'todo_all_employees.json'
    with open(file_name, 'w') as todo_file:
        json.dump(data, todo_file)


if __name__ == '__main__':
    all_users_tasks()
