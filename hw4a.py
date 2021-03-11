import requests
import json 

def github_repos():
  user_id =input("Type github user id")
  if(type(user_id)!= str):
    print("Invalid id")
    raise SystemExit
  x = requests.get(f"https://api.github.com/users/{user_id}/repos")
  get_json = x.json()
  if "message" in get_json:
    if get_json["message"] == "Not Found":
      print("User does not exist")
      raise SystemExit
  for i in get_json:
    repoName = i['name']

    commits = requests.get(f"https://api.github.com/repos/{user_id}/{repoName}/commits")
    y= commits.json()
    count = 0
    for x in y:
      if x['commit']:
        count+=1
    count = str(count)
    print("Repo: " + repoName + " Number of commits: " + count)

github_repos()