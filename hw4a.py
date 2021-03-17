import pip._vendor.requests
import json 
from pip._vendor import requests

def get_user_id(text):
  return input(text)
def github_repos():
  repos=""
  user_id = get_user_id("Github id")
  if(type(user_id)!= str):
    return("Invalid id")
  if(len(user_id) == 0 ):
    return("No id given")
  x = requests.get(f"https://api.github.com/users/{user_id}/repos")
  get_json = x.json()

  if "message" in get_json:
    if get_json["message"] == "Not Found":
      return("User does not exist")

  for i in get_json:
    if(i["name"]):
      repoName = i["name"]

    commits = requests.get(f"https://api.github.com/repos/{user_id}/{repoName}/commits")
    y= commits.json()
    count = 0
    for x in y:
      if x['commit']:
        count+=1
    count = str(count)
    s = "Repo: " + repoName + " Number of commits: " + count + '\n'
    repos+=s

  return repos

  

  
  


