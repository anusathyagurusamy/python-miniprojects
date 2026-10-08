import requests

url = input("Enter long URL: ")

api = f"https://tinyurl.com/api-create.php?url={url}"

short_url = requests.get(api).text

print(f"Short URL: {short_url}")