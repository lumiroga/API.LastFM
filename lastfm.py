import requests
import json

API_KEY = 'c4a34ba57da22b2fe7b7dc54d7768571'
USER_AGENT = 'Lumiroga/LastFM'

def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload['api_key'] = API_KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

r = lastfm_get({
    'method': 'chart.gettopartists'
})

jprint(r.json())