import requests
import json

ACCESS_TOKEN = "500752aa74ab91846753fc86c53f8e7cb27f5c81"

query_params = {
    'access_token': ACCESS_TOKEN,
    'longUrl': "http://en.wikipedia.org/wiki/Tetraodontidae"}
    
endpoint = "https://api-ssl.bitly.com/v3/shorten"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)
print data['data']['url']