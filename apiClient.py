import requests
import json

with open("token.txt") as f:
    token = f.read()
    
class restClient: # init of object with baseURL and token
    def __init__(self):
        self.token = token
        self.base_url = 'https://api.github.com'
        self.default_header = {"Authorization" : token}

    def get(self, path, params=None, headers=None):
        url = self.base_url + "/" + path
        final_headers = self.default_header
        if headers:
            final_headers.update(headers)
        try:
            response = requests.get(url, headers=final_headers, params=params)
            status_code = response.status_code
            return response, status_code
        except requests.RequestException as error:
            print("Error making GET request" + ":", error)
            return None, None

    def post(self, path, params=None, headers=None):
        pass

# Maybe move this to data formatter     
    def formatResponse(self, response):
        res = response.json()
        json_str = json.dumps(res, indent=2)
        return json_str
#



  ## we have init for authentication and holding the base url as variable
  # we will make functions to send requests
  # these should takebody and header parameters from main.py
  
  #Metoder:
  # Json.dumps() - serialzier et objekt, så hvis du f.eks har en dic {john : 1, mark : 2}, vil den omdanne til json struktur