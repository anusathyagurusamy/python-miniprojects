import requests

amount = float(input("Amount in INR: "))

data = requests.get(
    "https://api.exchangerate-api.com/v4/latest/INR"
).json()

usd = amount * data["rates"]["USD"]

print(f"{amount} INR = {usd:.2f} USD (live rate)")
