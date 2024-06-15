import requests

api_key = '0cb2360f-3c2b-4170-a32b-b8f34d224eae'
word = 'Potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

print(definitions)