# resource: https://www.datacamp.com/community/tutorials/meetup-api-data-json

import meetup.api
import json
import requests
import time
import codecs
import sys
import io

# better practice would be to save key locally then call it here
api_key = 'Your API Key Here' 

# one way to access Meetup group-specific data
client = meetup.api.Client(api_key)
group_info = client.GetGroup({'urlname':'Houston_PyLadies'})
print(group_info.name)