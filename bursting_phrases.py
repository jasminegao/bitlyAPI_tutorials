import requests
import json
import pprint
import settings

def getBurstingPhrases():
    query_params = {'access_token': settings.ACCESS_TOKEN}

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
