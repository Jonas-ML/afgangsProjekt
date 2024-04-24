import requests
from apiClient import *
import json

a = restClient()

response, status_code = a.get("repos/Jonas-ML/afgangsProjekt/commits", params={"sha":"dev"})

if status_code == 200:
    res = a.formatResponse(response)
else:
    print("ERROR CODE:", status_code)
    
