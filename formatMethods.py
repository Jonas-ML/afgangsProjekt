from apiClient import *


class dataFormatter:
    def __init__(self):
        pass
        
    def formatResponse(response): # Formats json string, to json object structure
        res = response.json()
        json_str = json.dumps(res, indent=2)
        return json_str


    def formatCommits(response, choosen_repo, choosen_Branch): # 
        data = json.loads(response)
        commit_details =""
        for commit in data:
            commit_message = commit['commit']['message']
            commit_date = commit['commit']['committer']['date']
            commit_details+= (
                 "================================================================================\n"
                f"Repository: {choosen_repo} on Branch: {choosen_Branch}\n"
                f"Commit: {commit_message}\n"
                f"Date:   {commit_date}\n"
                "--------------------------------------------------------------------------------\n"
            )
        return commit_details


    def fetchRepos(response): # Indexes the json object to extract repo names
        data = json.loads(response)
        repo_options = [repo['name'] for repo in data]
        return repo_options