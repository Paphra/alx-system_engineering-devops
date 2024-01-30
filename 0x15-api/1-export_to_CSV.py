#!/usr/bin/python3
"""1-export_to_CSV module
For a rest api that fetched employee data
"""
import csv
import json
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
    user_id = user_data.get('id')
    emp_name = user_data.get('name')

    todos_res = requests.get(todos_url)
    todos_data = todos_res.json()

    csv_file_name = "{}.csv".format(user_id)
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                str(user_id),
                emp_name,
                str(task['completed']),
                task['title']
            ])


if __name__ == '__main__':
    emp_id = int(sys.argv[1])
    employee_todo_progress(emp_id)
