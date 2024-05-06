from apiClient import *


def formatResponse(response): # Formats json string, to json object structure
    res = response.json()
    json_str = json.dumps(res, indent=2)
    return json_str


def formatCommits(response): # 
    data = json.loads(response)
    commit_details =""
    for commit in data:
        commit_message = commit['commit']['message']
        commit_date = commit['commit']['committer']['date']
        commit_details+= f"{commit_message} {commit_date}\n"
    return commit_details

def fetchRepos(repoRes): # Indexes the json object to extract repo names
    data = json.loads(repoRes)
    repo_options = [repo['name'] for repo in data]
    return repo_options