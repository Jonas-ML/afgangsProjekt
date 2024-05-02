import json

def fetchRepos(repoRes): # Indexes the json object to extract repo names
    data = json.loads(repoRes)
    repo_options = [repo['name'] for repo in data]
    return repo_options