import requests
import json
import pprint

ACCESS_TOKEN = "500752aa74ab91846753fc86c53f8e7cb27f5c81"

def getBurstingPhrases():
    query_params = {'access_token': ACCESS_TOKEN}

    endpoint = "https://api-ssl.bitly.com/v3/realtime/bursting_phrases"
    response = requests.get(endpoint, params = query_params)

    data = json.loads(response.content)

    phrases = []
    
    for item in data["data"]["phrases"]:
        info = {}
        info["phrase"] = item["phrase"]
        info["urls"] = item["urls"]
        phrases.append(info)
    
    for item in phrases:
        pprint.pprint(item)

if __name__ == '__main__':            
    getBurstingPhrases()
