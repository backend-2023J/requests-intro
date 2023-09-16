import requests

url = "https://randommer.io/api/Card"

headers = {
    "X-Api-Key": "f1ab06cd2da14928a4f4299e85162d76"
}
response = requests.get(url, headers=headers)

print(response.json())