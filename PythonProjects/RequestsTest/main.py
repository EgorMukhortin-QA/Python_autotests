import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'trainer_token'
HEADER = {'Countent-Type' : 'application/json', 'trainer_token' : TOKEN}

BODY_CREATE = { 
    "name": "generate",
    "photo_id": -1
}
BODY_CHANGE = {
    "pokemon_id": "343196",
    "name": "Name",
    "photo_id": 2
}
BODY_CHANGENAME = {
    "pokemon_id": "343196",
    "name": "New Name"
}
BODY_ADD = {
    "pokemon_id": "343196"
}
#Создание покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE)
print(response_create.json())

#Если put, то происходит изменение имени и аватара покемона, т.к. все поля обязательны в боди
response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGE)
print(response_change.json())

#смена имени
response_changename = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CHANGENAME)
print(response_changename.json())

#поймать покемона в покебол
response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = BODY_ADD)
print(response_add.json())
