import requests

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

r = lastfm_get({
    'method': 'chart.gettopartists'
})

print(r.status_code)