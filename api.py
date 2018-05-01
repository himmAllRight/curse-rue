import requests
import json

## Make a request to the Rue server API 
def rue_api_request(uri, url= None, category=None, verbose=False):
    payload = {'URL': url, 'Category': category}
    r = requests.post(uri, json=payload)

    if verbose:
        print("\nuri:", uri, "\n-----------------------------")
        print(r.status_code)
        print(r.json())

    return(r)


## Test Calls
rue_api_request("http://localhost:8080/get-feedstore"
                , verbose= True)

rue_api_request("http://localhost:8080/add-feed"
                , url= "http://ryan.himmelwright.net/post/index.xml"
                , category= "Development"
                , verbose= True)

rue_api_request("http://localhost:8080/get-all-feeditem-data"
                , url= "http://ryan.himmelwright.net/post/index.xml"
                , verbose= True)
