import requests
import json

## Just testing out how we'll make the API requests

r = requests.get('http://localhost:8080/get-feedstore')
print(r.status_code)
print(r.json())

# More complicated request... has a payload
payload = {'URL': "http://ryan.himmelwright.net/post/index.xml"}
r = requests.post('http://localhost:8080/get-all-feeditem-data', json=payload)
print(r.status_code)
print(r.json())



