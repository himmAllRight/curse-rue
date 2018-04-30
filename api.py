import requests

## Just testing out how we'll make the API requests

r = requests.get('http://localhost:8080/get-feedstore')
print(r.status_code)
print(r.json())


#payload = {'URL': "http://ryan.himmelwright.net/post/index.xml"}
#r = requests.get('http://localhost:8080/get-all-feeditem-data', params=payload)
#print(r.status_code)
#print(r.json())
