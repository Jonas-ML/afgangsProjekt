import requests
from apiClient import *
import json




headers = {
    'Authorization': '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',
    'Accept' : '*/*',
}
## "?sha=dev" is branch definition
r = requests.get("https://api.github.com/repos/Jonas-ML/afgangsProjekt/commits?sha=dev", headers=headers)

if r.status_code == 200:
    response_json = r.json()
    json_response = json.dumps(response_json, indent=2)
    print(json_response["message"])
else:
    print("Error", r.status_code)