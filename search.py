import pprint
import requests
import json

ACCESS_TOKEN = "53a01f38b09c0463cb9e2b35b151beb127843bf3"

query_params = {
    'access_token': ACCESS_TOKEN,
    'query': "food",
    'cities': "us-ny-brooklyn",
    'fields': "aggregate_link,title,url",
    'limit': 10}
        
endpoint = "https://api-ssl.bitly.com/v3/search"
response = requests.get(endpoint, params = query_params)
    
data = json.loads(response.content)

pprint.pprint(data['data']['results'])
