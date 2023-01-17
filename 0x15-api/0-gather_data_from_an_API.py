ing this.

REST API(https://jsonplaceholder.typicode.com/),
for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


def get_todos(emp_id: int):
    """Fetches TODO data for an employee from a given API endpoint.

    Keyword arguments:
    emp_id -- employee id parameter (integer)
    """
    url1 = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    userRequest = requests.get(url1)
    userdata = userRequest.json()
    username = userdata["name"]
    userId = userdata["id"]

    url = "https://jsonplaceholder.typicode.com/todos/"
    todosRequest = requests.get(url)
    todosData = todosRequest.json()
    todos = []
    total = 0
    completed = 0

    for todo in todosData:
        if todo["userId"] == userId:
            total += 1
            if todo["completed"] is True:
                completed += 1
                todos.append(todo["title"])

    print("Employee {} is done with tasks({}/{}):"
          .format(username, completed, total))
    for task in todos:
        print("\t {}".format(task))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_todos(sys.argv[1])
