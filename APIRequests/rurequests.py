import requests
import json
from datetime import datetime

parameters = {
    'lat': 40.71,
    'lon': -74
}

api_url = 'http://api.open-notify.org/iss-pass.json'

response = requests.get(api_url, params=parameters)
json_response = response.json()['response']
print(json_response)

risetimes = []

def using_json(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

for resp in json_response:
    risetimes.append(resp['risetime'])

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)