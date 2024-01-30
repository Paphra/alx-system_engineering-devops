#!/usr/bin/python3
"""0-gather_data_from_an_API module
For a rest api that fetched employee data
"""
import requests
import sys


def employee_todo_progress(emp_id):
    """Fetches and displays the employ todo progress
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, emp_id)
    todos_url = "{}/todos?userId={}".format(base_url, emp_id)

    user_response = requests.get(user_url)
    user_data = user_response.json()
    emp_name = user_data.get('name')

    todos_res = requests.get(todos_url)
    todos_data = todos_res.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    num_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks ({}/{}):".format(
        emp_name, num_of_done_tasks, total_tasks))
    for task in done_tasks:
        print("\t{}".format(task['title']))


if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    employee_todo_progress(emp_id)
