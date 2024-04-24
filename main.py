import requests
from apiClient import *
import json




""" headers = {
    'Authorization': token,
    'Accept' : '*/*',
}
## "?sha=dev" is branch definition
r = requests.get("https://api.github.com/repos/Jonas-ML/afgangsProjekt/commits?sha=dev", headers=headers)

if r.status_code == 200:
    response_json = r.json()
    json_response = json.dumps(response_json, indent=2)
    print(json_response)
else:
    print("Error", r.status_code) """
    
a = restClient()
response, status_code = a.get("repos/Jonas-ML/afgangsProjekt/commits", params={"sha":"dev"})
if status_code == 200:
    res = a.formatResponse(response)
    print(res)
else:
    print("ERROR CODE:", status_code)
    
