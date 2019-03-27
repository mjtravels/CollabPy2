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

mj_categories = [1,4,5,6,9,12,13,14,23,26,27,30,31,32,34]

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

# make an API call for each category MJ is interested in; store API responses in list
cats_pdx_requests = []
for cat in mj_categories:
    cats_pdx_requests.append(requests.get("https://api.meetup.com/find/groups?zip=97215&category_id="+str(cat)+"&key="+api_key).content)


# alternate way perform request, using params= as argument for requests.get()
# seems to return a 'Response' type
response2 = requests.get("http://api.meetup.com/find/groups", params={'city':'Portland','category_id':1,'key':api_key})

# normalize json data
# df = pd.DataFrame.from_dict(json_normalize(pdx_request), orient='columns')

# decode and load data into python object, then a dataframe
# cat1_pdx_df = pd.DataFrame.from_dict(json.loads(cat1_pdx_request.decode('utf-8')))


# STEP 1 OF CONVERTING JSON TO DATAFRAME: CONVERT JSON TO LIST OF DICTS
# split up dataframe creation - first load json object into list of dicts
# each list item is 1 group
# resource: https://stackoverflow.com/questions/19483351/converting-json-string-to-dictionary-not-list
cat1_pdx = json.loads(cat1_pdx_request.decode('utf-8'))

# data checks on above output:
type(cat1_pdx)
len(cat1_pdx)
cat1_pdx[2]

# STEP 2 OF CONVERTING JSON TO DATAFRAME: NORMALIZE LIST OF DICTS INTO DF
# resource: https://stackoverflow.com/questions/20638006/convert-list-of-dictionaries-to-a-pandas-dataframe/53831756#53831756
cat1_pdx_df = pd.io.json.json_normalize(cat1_pdx)

# data checks on above output:
type(cat1_pdx_df)
cat1_pdx_df.head()
cat1_pdx_df3.count()
cat1_pdx_df3.groupby('category.id').count()
