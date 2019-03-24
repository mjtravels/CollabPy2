# resource: https://www.datacamp.com/community/tutorials/meetup-api-data-json

import meetup.api
import json
import requests
import time
import codecs
import sys
import io

# access API key saved in a api_key.txt file locally
api_file = open("api_key.txt", "r")
api_key = api_file.read()
api_file.close

# one way to access Meetup group-specific data
client = meetup.api.Client(api_key)
group_info = client.GetGroup({'urlname':'Houston_PyLadies'})

# search by zip code directly - using requests
request = requests.get("https://api.meetup.com/find/groups?zip=11211&key="+api_key)
