import requests
import json
import pprint

ACCESS_TOKEN = "53a01f38b09c0463cb9e2b35b151beb127843bf3"

query_params = {
    'access_token': ACCESS_TOKEN,
	'title': "Chipotle is great",
	'description': "Only the best links to stuff about Chipotle",
	'private': "false"}
	
endpoint = "https://api-ssl.bitly.com/v3/bundle/create"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

pprint.pprint(data['data']['bundle'], indent = 3)