from apiClient import *

a = restClient()








def formatResponse(response): # Formats json string, to json object structure
    res = response.json()
    json_str = json.dumps(res, indent=2)
    return json_str


def formatCommits(response): # 
    data = json.loads(response)
    for commit in data:
        commit_message = commit['commit']['message']
        commit_date = commit['commit']['committer']['date']
        print(commit_message, commit_date)
