import requests
import json


def retrieve_from_api(api):
    response = requests.get(f"https://pokeapi.co/api/v2/{api}")
    if response.status_code == 200:
        data = response.text
        some = json.loads(data)
        return some
    return False


def by_type():
    pokemons = retrieve_from_api('type')['results']
    return pokemons


def type_by_id(type_id):
    pokemons = retrieve_from_api(f'type/{type_id}')
    return pokemons

def poke_by_id(name_id):
    pokemons = retrieve_from_api(f'pokemon/{name_id}')
    return pokemons

def all_pokemons():
    pokemons = retrieve_from_api(f'pokemon')
    return pokemons
