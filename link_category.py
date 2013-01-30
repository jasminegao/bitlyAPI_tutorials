import requests
import json
import pprint

ACCESS_TOKEN = "53a01f38b09c0463cb9e2b35b151beb127843bf3"

query_params = {
    'access_token': ACCESS_TOKEN,
    'link': "http://worrydream.com/LearnableProgramming/"}

endpoint = "https://api-ssl.bitly.com/v3/link/category"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

pprint.pprint(data['data'], indent = 3)