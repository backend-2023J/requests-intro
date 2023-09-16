import requests

url = "https://randommer.io/api/Finance/CryptoAddress"

headers = {
    "X-Api-Key": "f1ab06cd2da14928a4f4299e85162d76"
}
parameters = {
    "cryptoType": "Bitcoinplus"
}
response = requests.get(url, params=parameters, headers=headers)

print(response.json())

# ['Argoneum', 'BCash', 'BGold', 'BitCore', 'Bitcoin', 'Dash', 'Dogecoin', 'Verge', 'Dystem', 'Feathercoin', 'Groestlcoin', 'Liquid', 'Litecoin', 'Monacoin', 'Polis', 'Terracoin', 'UFO', 'Viacoin', 'Zclassic', 'Koto', 'Bitcoinplus', 'Chaincoin', 'ZCoin', 'DogeCash', 'Ethereum']