import json


class dataFormatter:
    def __init__(self):
        pass
        
    def fetchRepos(self, response): 
        try:
            data = json.loads(response) #deserializer til et python objekt
            repo_options = [repo['name'] for repo in data] # finder "name" key og tager value
            return repo_options 
        except Exception as e:
            print(f"An error occurred while fetching repos: {e}")

    
    def formatResponse(self, response):
        try:
            res = response.json()
            json_str = json.dumps(res, indent=2) #Json object til Json string
            return json_str
        except Exception as e:
            print(f"An error occurred while formatting the response: {e}")


    def formatCommits(self, response, choosen_repo, choosen_Branch):
        try:
            data = json.loads(response)
            commit_details = ""
            for commit in data:
                commit_message = commit['commit']['message']
                commit_date = commit['commit']['committer']['date'] # Indexerer objektet for at finde de rigtige keys til at putte ind i string
                commit_details += (
                    "============================================================================\n"
                    f"Repository: {choosen_repo} on Branch: {choosen_Branch}\n"
                    f"Commit: {commit_message}\n"
                    f"Date:   {commit_date}\n"
                )
            return commit_details
        except Exception as e:
            print(f"An error occurred while formatting commits: {e}")

    def textFormatting(self, txt, keywords):
        try:
            rearranged_commits = ""
            for keyword in keywords:  # tager keywords fra dialog box i formattxt
                if keyword.strip() != "": # tjekker om der er et keyword -- LINJEN UNDER splitter texten og søger efter matchende commits. SPLIT - splitter txt til en liste af commits
                    keyword_commits = [commit.strip() for commit in txt.split("============================================================================") if keyword.strip().lower() in commit.lower()]# tjekker om keyword er fundet i commit txt
                    for commit in keyword_commits:# tager de foramterede commits og looper dem ud på skærmen
                        rearranged_commits += (
                            "============================================================================\n"
                            f"{commit}\n"
                        )
            return rearranged_commits
        except Exception as e:
            print(f"An error occurred while formatting commits: {e}")




