import requests
import json

ACCESS_TOKEN = "53a01f38b09c0463cb9e2b35b151beb127843bf3"

query_params = {
    'access_token': ACCESS_TOKEN,
    'longUrl': raw_input("Enter a long url you want to shorten: ")}
    
endpoint = "https://api-ssl.bitly.com/v3/shorten"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)
print "Voila!" + "   " + str(data['data']['url'])