import requests
import json
import pprint
import settings

query_params = {
    'access_token': "your_access_token",
	'title': "Chipotle is great",
	'description': "Only the best links to stuff about Chipotle",
	'private': "false"}
	
endpoint = "https://api-ssl.bitly.com/v3/bundle/create"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

pprint.pprint(data['data']['bundle'], indent = 3)
