import requests
import json
import pprint

query_params = {
    'access_token': settings.ACCESS_TOKEN,
    'link': "http://worrydream.com/LearnableProgramming/"}

endpoint = "https://api-ssl.bitly.com/v3/link/category"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

pprint.pprint(data['data'], indent = 3)
