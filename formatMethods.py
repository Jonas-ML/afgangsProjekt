from apiClient import *


class dataFormatter:
    def __init__(self):
        pass
        
    def fetchRepos(self, response): # Indexes the json object to extract repo names
        data = json.loads(response)
        repo_options = [repo['name'] for repo in data]
        return repo_options    
    
    def formatResponse(self, response): # Formats json string, to json object structure
        res = response.json()
        json_str = json.dumps(res, indent=2)
        return json_str

    def formatCommits(self, response, choosen_repo, choosen_Branch): # 
        data = json.loads(response)
        commit_details = ""
        for commit in data:
            commit_message = commit['commit']['message']
            commit_date = commit['commit']['committer']['date']
            commit_details += (
                 "================================================================================\n"
                f"Repository: {choosen_repo} on Branch: {choosen_Branch}\n"
                f"Commit: {commit_message}\n"
                f"Date:   {commit_date}\n"
            )
        return commit_details

    def textFormatting(self, txt, keywords):
        try:
            rearranged_commits = ""
            for keyword in keywords:
                if keyword.strip() != "":
                    keyword_commits = [commit.strip() for commit in txt.split("================================================================================") if keyword.strip().lower() in commit.lower()]
                    rearranged_commits += "\n".join(keyword_commits) + ";\n"  # Separating commits by semicolons
            return rearranged_commits
        except Exception as e:
            print(f"An error occurred while formatting commits: {e}")




