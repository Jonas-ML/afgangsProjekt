import requests

class restClient:
    def __init__(self, token):
        self.token = token
        self.base_url = 'https://api.github.com'

    def get(self, path):
        self.base_url + "/" + path

    def post(self, path):
        self.base_url + "/" + path

  ## we have init for authentication and holding the base url as variable
  # we will make functions to send requests
  # these should take body and header parameters from main.py