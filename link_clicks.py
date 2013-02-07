import requests
import json
import pprint
import settings

query_params = {
    'access_token': settings.ACCESS_TOKEN,
    'link': "http://bitly.com/RYYpZT",
    'unit': "minute",
    'units': 60}

endpoint = "https://api-ssl.bitly.com/v3/link/clicks"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

pprint.pprint(data['data']['link_clicks'])
