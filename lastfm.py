import requests

API_KEY = 'c4a34ba57da22b2fe7b7dc54d7768571'
USER_AGENT = 'Lumiroga/LastFM'

headers = {
    'user-agent': USER_AGENT
}

payload = {
    'api_key': API_KEY,
    'method': 'chart.gettopartists',
    'format': 'json'
}

r = requests.get('http://ws.audioscrobbler.com/2.0/', headers=headers, params=payload)
r.status_code