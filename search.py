import pprint
import requests
import json

ACCESS_TOKEN = "500752aa74ab91846753fc86c53f8e7cb27f5c81"

query_params = {
    'access_token': ACCESS_TOKEN,
    'query': "food",
    'cities': "us-ny-brooklyn",
    'fields': "aggregate_link,title,url",
    'limit': 10}
        
endpoint = "https://api-ssl.bitly.com/v3/search"
response = requests.get(endpoint, params = query_params)
    
data = json.loads(response.content)

pprint.pprint(data['data']['results'], indent = 3)
