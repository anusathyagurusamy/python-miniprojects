import requests

username = input("GitHub username: ")

url = f"https://api.github.com/users/{username}"

data = requests.get(url).json()

print(f"Name: {data.get('name')}")
print(f"Public Repos: {data.get('public_repos')}")
print(f"Followers: {data.get('followers')}")