import requests
import sys
import os

github_api_token = os.environ['GITHUB_TOKEN']

url  = 'https://api.github.com/users/'
headers = {
    'Authorization': 'Bearer ' + github_api_token
}

github_base_url = 'https://api.github.com/repos/'



git_repo = str(sys.argv[1])


def get_user_location(url):
    response = requests.request("GET", url, headers=headers)
    return response.json()


def get_repo_contributors(url):
    response = requests.request("GET", url=url, headers=headers)
    return response.json()


print("Fetching contributors / locations for " + git_repo)
for contributor in get_repo_contributors(github_base_url + git_repo + "/contributors"):
    print (contributor['login'] + " - ", end='')
    print (get_user_location(url + contributor["login"])["location"])

