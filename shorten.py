import requests
import json
import settings

query_params = {
    'access_token': settings.ACCESS_TOKEN,
    'longUrl': "http://en.wikipedia.org/wiki/Tetraodontidae"}
    
endpoint = "https://api-ssl.bitly.com/v3/shorten"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)
print data['data']['url']
