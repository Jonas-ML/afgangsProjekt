from apiClient import *


class dataFormatter:
    def __init__(self):
        pass
        
    def fetchRepos(self, response): 
        try:
            data = json.loads(response)
            repo_options = [repo['name'] for repo in data]
            return repo_options 
        except json.JSONDecodeError as e: # Syntax errors, missing contents, unsupported data types
            print(f"An error occurred while decoding JSON: {e}")
        except Exception as e:
            print(f"An error occurred while fetching repos: {e}")

    
    def formatResponse(self, response):
        try:
            res = response.json()
            json_str = json.dumps(res, indent=2)
            return json_str
        except Exception as e:
            print(f"An error occurred while formatting the response: {e}")


    def formatCommits(self, response, choosen_repo, choosen_Branch):
        try:
            data = json.loads(response)
            commit_details = ""
            for commit in data:
                commit_message = commit['commit']['message']
                commit_date = commit['commit']['committer']['date']
                commit_details += (
                    "============================================================================\n"
                    f"Repository: {choosen_repo} on Branch: {choosen_Branch}\n"
                    f"Commit: {commit_message}\n"
                    f"Date:   {commit_date}\n"
                )
            return commit_details
        except json.JSONDecodeError as e: # Syntax errors, missing contents, unsupported data types
            print(f"An error occurred while decoding JSON: {e}")
        except KeyError as e: # If you try to find a key that doesnt exist
            print(f"Missing key in JSON data: {e}")
        except Exception as e:
            print(f"An error occurred while formatting commits: {e}")

    def textFormatting(self, txt, keywords):
        try:
            rearranged_commits = ""
            for keyword in keywords:
                if keyword.strip() != "":
                    keyword_commits = [commit.strip() for commit in txt.split("============================================================================") if keyword.strip().lower() in commit.lower()]
                    for commit in keyword_commits:
                        rearranged_commits += (
                            "============================================================================\n"
                            f"{commit}\n"
                        )
            return rearranged_commits
        except Exception as e:
            print(f"An error occurred while formatting commits: {e}")




