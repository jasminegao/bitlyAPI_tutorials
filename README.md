bitlyAPI_tutorials
===================

The following are simple tutorials to help get you started on using
bitly's APIs. For these tutorials we will be using a generic access
token generated for the bitlyapitutorials account. To get your own
access token, [click here](https://bitly.com/a/oauth_apps) to generate
one on bitly.com or visit our [OAuth documentation](http://dev.bitly.com/authentication.html) for a walkthrough of the authentication process. 

Listed are tutorials to perform the following:

* Shortening a link
* Finding the categories of a webpage
* Getting the number of clicks on a link
* Returning phrases bursting in popularity
* Searching all bitly links receiving clicks
* Creating a bundle
* Adding a link to a bundle

<a id="shorten"></a>Shortening a link
------------------------------------------------------------------ 

To shorten a link, you simply connect to the [/v3/shorten](http://dev.bitly.com/links.html#v3_shorten) endpoint and pass a webpage link as the `longUrl` parameter:

```python
import requests
import json

ACCESS_TOKEN = "500752aa74ab91846753fc86c53f8e7cb27f5c81"

query_ params = {
	'access_token': ACCESS_TOKEN,
	'longUrl': "http://worrydream.com/LearnableProgramming/"}

endpoint = "https://api-ssl.bitly.com/v3/shorten"
response = requests.get(endpoint, params_params)

data = json.loads(response.content)

print data['data']['url']

```
In the above code, the JSON response is a dictionary with several values and we print out just the short url found in the `['data']['url']` key. 

<a id="categories"></a>Finding the categories of a webpage
------------------------------------------------------------------

A webpage can be about food, technology, entertainment or just about anything. At bitly, we label each webpage with the categories it's most likely to fall under. To return the categories of a webpage, you can use a method similar to shortening a link by connecting to the [/v3/link/category](http://dev.bitly.com/data_apis.html#v3_link_category) endpoint and passing a bitly short url as the `link` parameter:

```python
import requests
import json

ACCESS_TOKEN = "500752aa74ab91846753fc86c53f8e7cb27f5c81"

query_ params = {
	'access_token': ACCESS_TOKEN,
	'link': "data['data']['url']"}

endpoint = "https://api-ssl.bitly.com/v3/link/category"
response = requests.get(endpoint, params_params)

data = json.loads(response.content)

print data['data']['categories']
```
Here, we use the short url found in the JSON response of the previous example as the `link` parameter (however, you may also simply pass any bitly short url like so: `'link': "http://bitly.com/RYYpZT"`) and print out the detected categories for the page in descending order of confidence. 

<a id="clicks"></a>Getting the number of clicks on a bitly link
------------------------------------------------------------------

Did you know you could view the stats for any bitly link by adding a plus sign (+) to the end of it (like this: http://bitly.com/RYYpZT+)? It's just as easy to get the stats and, more specifically, the number of clicks on a bitly link programmatically as well. All you have to do is connect to the  [/v3/link/clicks](http://dev.bitly.com/link_metrics.html#v3_link_clicks) endpoint and pass a bitly short url as the `link` parameter:

```python
import requests
import json

ACCESS_TOKEN = "500752aa74ab91846753fc86c53f8e7cb27f5c81"

query_params = {
        'access_token': ACCESS_TOKEN,
        'link': "http://bitly.com/RYYpZT",
        'unit': "minute",
        'units': 60}

endpoint = "https://api-ssl.bitly.com/v3/link/clicks"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

print data['data']['link_clicks']
```
In this example, we made use of two new parameters unique to the /v3/link/clicks endpoint: `unit` and `units` which specify the 
measure and period, respectively, of time to query data for. As a result, the number of clicks on `http://bitly.com/RYYpZT` in past 60 minutes are printed. 

<a id="bursting"></a>Returning phrases bursting in popularity
----------------------------------------------------------------------

When webpages containing the same phrase(s) receive uncharacteristically high click traffic, we say the phrase(s) is bursting. This gives us a good idea of what the internet is paying attention to. To find out what phrases are currently bursting and which links are driving traffic to webpages containing those phrases, you can use the [/v3/realtime/bursting_phrases](http://dev.bitly.com/data_apis.html#v3_realtime_bursting_phrases) endpoint. 

```python
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
```
Viewing data on current bursting phrases can be done by just printing the JSON response. However, in this example script, we create an empty list called `phrases` in which we nest the dictionary `info` containing only the `phrase` and `urls` key value pairs. This returns a list of bursting phrases as well as all the bitly links pointing to webpages containing those phrases and the visitors for each. 

<a id="search"></a>Search all bitly links receiving clicks
------------------------------------------------------------

Bursting phrases may also be fed into our search API, which powers our search engine [rt.ly](rt.ly), by using the [/v3/search](http://dev.bitly.com/data_apis.html#v3_search) endpoint and setting the `query` parameter to a phrase. You can also search normally and filter results by topic, social network, city, domain and language: 

```python
import requests
import json
import pprint

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
```
In the above script, we are searching for links to 10 pieces of content related to food being read by people in Brooklyn, NY and printing the `aggregate_link` (short url), `title` and `url` (long url) for each. A full list of parameters can found in the /v3/search documentation [here](http://dev.bitly.com/data_apis.html#v3_search).

<a id="createbundle"></a>Create a bundle
----------------------------------------
Bundles are great for organizing all of your saved bitly links into collections and make sharing multiple links quick and easy. By connecting to the [/v3/bundle/create](http://dev.bitly.com/bundles.html#v3_bundle_create) endpoint you can create a bundle, title it, add a description and set it as public or private:

```python
import requests
import json
import pprint

ACCESS_TOKEN = "500752aa74ab91846753fc86c53f8e7cb27f5c81"

query_params = {
    'access_token': ACCESS_TOKEN,
	'title': "Chipotle is great",
	'description': "Only the best links to stuff about Chipotle",
	'private': "false"}
	
endpoint = "https://api-ssl.bitly.com/v3/bundle/create"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

pprint.pprint(data['data']['bundle'], indent = 3)
```

<a id="addlinktobundle"></a>Add a link to a bundle
------------------------------------------------
To add a link to your newly created bundle, simply use the [/v3/bundle/link_add](http://dev.bitly.com/bundles.html#v3_bundle_link_add) endpoint and pass the link into the `link` parameter:

```python
import requests
import json
import pprint

ACCESS_TOKEN = "500752aa74ab91846753fc86c53f8e7cb27f5c81"

query_params = {
    'access_token': ACCESS_TOKEN,
	'bundle_link': "http://bitly.com/bundles/bitlyapitutorials/1",
    'link': "http://thoughtcatalog.com/2012/how-to-hack-chipotle/"}
	
endpoint = "https://api-ssl.bitly.com/v3/bundle/link_add"
response = requests.get(endpoint, params = query_params)

data = json.loads(response.content)

pprint.pprint(data['data']['bundle'], indent = 3)
```
Here, the `bundle_link` is one of the return values you get after creating a bundle but can also be found via your browser's address bar. Additionally, in this example, the link to be added to the bundle is a long url but any bitly short url can be used as well. 
