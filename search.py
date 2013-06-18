import pprint
import requests
import json
import settings

query_params = {
    'access_token': "your_access_token",
    'query': "food",
    'cities': "us-ny-brooklyn",
    'fields': "aggregate_link,title,url",
    'limit': 10}
        
endpoint = "https://api-ssl.bitly.com/v3/search"
response = requests.get(endpoint, params = query_params)
    
data = json.loads(response.content)

pprint.pprint(data['data']['results'], indent = 3)
