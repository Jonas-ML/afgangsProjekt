import requests

class restClient:
    def __init__(self, token):
        self.token = token
        self.base_url = 'https://api.github.com'

    def get(self, path):
        self.base_url + "/" + path

    def post(self, path):
        self.base_url + "/" + path

  