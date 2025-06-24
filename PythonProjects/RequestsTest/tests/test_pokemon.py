import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'trainer_token'
HEADER = {'Countent-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '36352'

def tests_status_code():
    response_code = requests.get(url = f'{URL}/trainers')
    assert response_code.status_code == 200

def tests_my_name():
    response_name = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response_name.json()['data'][0]['trainer_name'] == 'Toy'