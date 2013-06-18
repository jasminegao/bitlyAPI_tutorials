import requests
import json
import pprint
import settings

query_params = {
    'access_token': "your_access_token",
	'bundle_link': "http://bitly.com/bundles/bitlyapitutorials/1",
    'link': "http://thoughtcatalog.com/2012/how-to-hack-chipotle/"}
	
endpoint = "https://api-ssl.bitly.com/v3/bundle/link_add"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

pprint.pprint(data['data']['bundle'], indent = 3)
