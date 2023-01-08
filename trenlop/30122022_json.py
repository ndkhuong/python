import requests
import json

api_url = 'https://www.jsonkeeper.com/b/D8TC'
rs = requests.get(api_url)
obj = rs.json()
print(rs.status_code)
print(rs.headers["content-type"])