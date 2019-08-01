import requests

for poke_number in range(1, 152):
#poke_number = 4
    r = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(poke_number))
    poke_name = r.json()['forms'][0]['name']
#poke_type = r.json()['types'][1]['type']['name']
    poke_url = r.json()['sprites']['front_default']
    print([poke_name, poke_url])