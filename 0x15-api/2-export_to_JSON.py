#!/usr/bin/python3
"""0-gather_data_from_an_API module
For a rest api that fetched employee data
"""
import json
import requests
import sys


def employee_todo_progress(emp_id):
    """Fetches and displays the employ todo progress
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, emp_id)
    todos_url = "{}/todos".format(user_url)

    user_response = requests.get(user_url)
    user_data = user_response.json()
    emp_name = user_data.get('name')

    todos_res = requests.get(todos_url)
    todos_data = todos_res.json()

    export_data = {
        str(emp_id): [
            {
                'task': task['title'],
                'completed': task['completed'],
                'username': emp_name
            } for task in todos_data
        ]
    }

    json_filename = '{}.json'.format(emp_id)
    with open(json_filename, 'w') as json_file:
        json.dump(export_data, json_file)


if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    employee_todo_progress(emp_id)
