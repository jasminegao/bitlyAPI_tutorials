import requests
import json
import pprint

ACCESS_TOKEN = "500752aa74ab91846753fc86c53f8e7cb27f5c81"

query_params = {
    'access_token': ACCESS_TOKEN,
	'title': "Chipotle is great",
	'description': "Only the best links to stuff about Chipotle",
	'private': "false"}
	
endpoint = "https://api-ssl.bitly.com/v3/bundle/create"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

pprint.pprint(data['data']['bundle'], indent = 3)