from apiClient import *

a = restClient()

response, status_code = a.get("repos/Jonas-ML/afgangsProjekt/commits", params={"sha":"dev"})

if status_code == 200:
    res = a.formatResponse(response)
else:
    print("ERROR CODE:", status_code)
    


data = json.loads(res)


for commit in data:
    commit_message = commit['commit']['message']
    commit_date = commit['commit']['committer']['date']
    print(commit_message, commit_date)
