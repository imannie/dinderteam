import requests
from header_for_request import header

response = requests.get("https://api.yelp.com/v3/autocomplete?text=del&latitude=37.786882&longitude=-122.399972", headers=header)
data = response.json()
print(data)

