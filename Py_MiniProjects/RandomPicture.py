import requests

url = "https://picsum.photos/1920/1080"
response = requests.get(url)

with open("wallpaper.jpg", "wb") as f:
    f.write(response.content)

print("Wallpaper saved ✅")