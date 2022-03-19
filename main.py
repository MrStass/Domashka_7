import csv
import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')
response_user_name = response.json()


for user in response_user_name:
    with open(f'{user["name"]}.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'title', 'completed'])
        writer.writeheader()
        todos = requests.get(f'{"https://jsonplaceholder.typicode.com/todos"}?userId={user["id"]}')
        tod = todos.json()
        for obj in tod:
            obj.pop('userId')
        for todo in tod:
            writer.writerow(todo)
