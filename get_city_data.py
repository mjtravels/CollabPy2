# resource: https://www.datacamp.com/community/tutorials/meetup-api-data-json

import meetup.api
from info import logins
import json
import requests
import time
import codecs
import sys
import io
import pandas as pd
from pandas.io.json import json_normalize
import numpy as np

# access API key saved in a api_key.txt file locally
# api_file = open("api_key.txt", "r")
# api_key = api_file.read()
# api_file.close

# access API key saved in info.py with other credentials
api_key = logins["meetup"]["api_key"]

# one way to access Meetup group-specific data
client = meetup.api.Client(api_key)
group_info = client.GetGroup({'urlname':'Houston_PyLadies'})

# search by zip code directly - using requests
pdx_request = requests.get("https://api.meetup.com/find/groups?zip=97215&key="+api_key)
# limit request to 1 category in 1 zip code
cat1_pdx_request = requests.get("https://api.meetup.com/find/groups?zip=97215&category_id=1&key="+api_key).content

# normalize json data
df = pd.DataFrame.from_dict(json_normalize(pdx_request), orient='columns')

# decode and load data into python object
cat1_pdx_df = json.loads(cat1_pdx_request.decode('utf-8'))