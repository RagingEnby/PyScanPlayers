import requests
import json
from send_webhook import send_webhook
with open('config.json', 'r') as file:
    config = json.load(file)

def verify_json():
    for player in config['players']:
        player['ign'] = requests.get(f'https://api.ragingenby.dev/ign/{player["uuid"]}?key={config["ragingenby_api_key"]}').json()['name']
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=2)

def get_status(uuid):
    response = requests.get(f'https://api.hypixel.net/status?key={config["hypixel_api_key"]}&uuid={uuid}')
    if response.status_code == 200:
        print(response.json())
    else:
        return False,

def main():
    verify_json()
    for player in config["players"]:
        get_status(player['uuid'])


    exit()


while True:
    main()
