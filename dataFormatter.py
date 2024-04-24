from main import *
import json

data = json.loads(res)
search = "message"

for commit in data:
    commit_message = commit['commit']['message']
    commit_date = commit['commit']['committer']['date']
    print(commit_message, commit_date)
