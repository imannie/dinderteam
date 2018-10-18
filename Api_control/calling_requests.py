import requests
import json
from header_for_request import header
import pprint

pp = pprint.PrettyPrinter(indent=4)

#header has the authorization for the api
response = requests.get("https://api.yelp.com/v3/businesses/search?term=food&location=oakland", headers=header)
data = response.json() #turns the api response into a json
pp.pprint(data)

# #this allows us to pick out specific things
# for x in data['businesses']:
#     print(x['image_url'],"\n")