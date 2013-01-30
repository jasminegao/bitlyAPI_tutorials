bitlyAPI_tutorials
===================

The following are simple tutorials to help get you started on using bitly's APIs. Before you begin, it is assumed you have registered an application and generated an access token. If not, you can visit our [OAuth documentation](http://dev.bitly.com/authentication.html) for a walkthrough of the authentication process. 

Shortening a link
------------------------------------------------------------------

This tutorial will guide you through performing what bitly is most well known for: shortening a link and returning data on it. 

To shorten a link, you simply connect to the [/v3/shorten](http://dev.bitly.com/links.html#v3_shorten) endpoint and pass a webpage link as the `'longUrl'` parameter:

```python
import requests
import json

ACCESS_TOKEN = "53a01f38b09c0463cb9e2b35b151beb127843bf3"

query_ params = {
	'access_token': ACCESS_TOKEN,
	'longUrl': "http://worrydream.com/LearnableProgramming/"}

endpoint = "https://api-ssl.bitly.com/v3/shorten"
response = requests.get(endpoint, params_params)

data = json.loads(response.content)
print data['data']['url']

```
In the above code, the JSON response is a dictionary with several values and we print out just the short url found in the `['data']['url']` key. 

Finding the categoires of a webpage
------------------------------------------------------------------

A webpage can be about food, technology, entertainment or just about anything. At bitly, we label each webpage with the categories it's most likely to fall under. To return the categories of a webpage, you can use a method similar to shortening a link by connecting to the [/v3/link/category](http://dev.bitly.com/data_apis.html#v3_link_category) endpoint and passing a bitly short url as the `'link'` parameter:

```python
query_ params = {
	'access_token': ACCESS_TOKEN,
	'link': "data['data']['url']"}

endpoint = "https://api-ssl.bitly.com/v3/link/category"
response = requests.get(endpoint, params_params)

data = json.loads(response.content)
print data['data']['categories']
```
Here, we use the short url found in the JSON response of the previous example as the `'link'` parameter (however, you may also simply pass any bitly short url like so: `'link': "http://bitly.com/RYYpZT"`) and print out the detected categories for the page in descending order of confidence. 

Getting the number of clicks on a bitly link
------------------------------------------------------------------

Did you know you could view the stats for any bitly link by adding a plus sign (+) to the end of it (like this: http://bitly.com/RYYpZT+)? It's just as easy to get the stats and, more specifically, the number of clicks on a bitly link programmatically as well. All you have to do is connect to the  [/v3/link/clicks](http://dev.bitly.com/link_metrics.html#v3_link_clicks) endpoint and pass a bitly short url as the `'link'` parameter:

```python
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

<a id="bursting"></a>Return bursting phrases
--------------------------------------------
Endpoint: [/v3/realtime/bursting_phrases](http://dev.bitly.com/data_apis.html#v3_realtime_bursting_phrases)

<a id="search"></a>Search all bitly links receiving clicks
----------------------------------------------------------
Endpoint: [/v3/search](http://dev.bitly.com/data_apis.html#v3_search)

<a id="createbundle"></a>Create a bundle
----------------------------------------
Endpoint: [/v3/bundle/create](http://dev.bitly.com/bundles.html#v3_bundle_create)

<a id="addlinktobundle"></a>Add a link to a bundle
------------------------------------------------
Endpoint: [/v3/bundle/link_add](http://dev.bitly.com/bundles.html#v3_bundle_link_add)


