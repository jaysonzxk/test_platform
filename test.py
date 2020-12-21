import requests

url = "http://127.0.0.1:5000/query/userInfo"

payload={}
headers = {
  'x-token': 'eyJhbGciOiJIUzI1NiIsImlhdCI6MTYwNzQ3OTEwOSwiZXhwIjoxNjA3NDgyNzA5fQ.eyJuYW1lIjoiYWRtaW4ifQ.OD9KmllaNCBv7sR6UYibp_NqBATuHwKKBwN7QsqOfB8'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json().get('data').get('username'))