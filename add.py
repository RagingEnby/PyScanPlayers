import json
import requests
import datetime
from send_webhook import send_webhook

with open('config.json', 'r') as file:
    config = json.load(file)

def get_uuid(ign):
    try:
        response = requests.get(f'https://api.ragingenby.dev/uuid/{ign}?key={config["ragingenby_api_key"]}').json()
        return response['id'], response['name']
    except Exception:
        return None, None

while True:
    input_ign = input('Who would you like to add? > ')
    uuid, ign = get_uuid(input_ign)
    if uuid is None:
        exit('invalid ign')

    reason = input('Why are you adding them? > ')
    ping = input('Would you like to be pinged for them (default yes)? > ')
    if ping == '': ping = True
    playerData = {
        "uuid": uuid,
        "ign": ign,
        "reason": reason,
        "ping": bool(ping),
        "onlineData": {
            "online": False,
            "session": {}
        }
    }
    config['players'].append(playerData)
    with open('config.json', 'w') as file:
        json.dump(config, file, indent=2)
    send_webhook(playerData, "added", config)
    print('\n\n')