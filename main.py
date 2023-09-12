import requests

url = 'https://randomuser.me/api/'

def get_headers(url: str) -> dict:

    response = requests.get(url)
    data = response.json()

    return response.status_code

print(get_headers(url))