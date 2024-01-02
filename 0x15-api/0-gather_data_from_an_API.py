#!/usr/bin/python3
"""returns information about his/her TODO list progress.."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed_tasks = [task["title"] for task in todos if task["completed"]]
    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(completed_tasks), len(todos)))

    [print("\t {}".format(task)) for task in completed_tasks]
