import requests
import json
import pprint

ACCESS_TOKEN = "53a01f38b09c0463cb9e2b35b151beb127843bf3"

query_params = {
    'access_token': ACCESS_TOKEN,
	'bundle_link': "http://bitly.com/bundles/jasminegao/k",
    'link': raw_input("Enter a bitly short url or long url that you want added to this bundle: ")}
	
endpoint = "https://api-ssl.bitly.com/v3/bundle/link_add"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

pprint.pprint(data['data']['bundle'], indent = 3)