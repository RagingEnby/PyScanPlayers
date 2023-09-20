import json
import requests
import datetime

def send_webhook(player, status_change, config):
    print('send_webhook')
    if status_change != "added": title = f"{player['ign']} {status_change} Hypixel!"
    else: title = f"{player['ign']} added to the tracker!"

    content = player['reason']
    if player['ping']: content = config['webhook']['ping'] + ' ' + content
    webhook = {
        "content": content,
        "embeds": [
            {
                "title": title,
                #"description": f"{player['ign']} {status_change} Hypixel!",
                "color": config['webhook']['embedColor'][status_change],
                "author": {
                    "name": player['ign'],
                    "icon_url": f"https://mc-heads.net/head/{player['uuid']}"
                }
            }
        ],
        "username": config['webhook']['profile']['username'],
        "avatar_url": config['webhook']['profile']['avatar'],
        "timestamp": f"{datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'}"
    }
    requests.post(config['webhook']['url'], data=json.dumps(webhook), headers={"Content-Type": "application/json"})
