import requests
import json

# requests.get()
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code) # 200

# response.json() & json.dumps (Pretty print)
data = response.json()
json_string = json.dumps(data, indent=2)
print(json_string)

# json.loads() - String to Dict
parsed = json.loads('{"active": true}')