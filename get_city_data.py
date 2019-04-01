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

mj_cats = [1,4,5,6,9,12,13,14,23,26,27,30,31,32,34]
example_mj_cats = [1,4,5]
mj_cities = []
example_mj_cities = ['Portland']

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
# limit request to 3 categories in 1 zip code as example
cat1_pdx_request = requests.get("https://api.meetup.com/find/groups?zip=97215&category=1,4,5&key="+api_key).content

# make an API call for each category MJ is interested in; store API responses in list
# need to revise because New Age & Sprituality shouldn't be a result
cats_pdx_requests = []
for cat in example_mj_cats:
    # append individual cat responses, decoded and turned into df in same step
    cats_pdx_requests.append(pd.io.json.json_normalize(json.loads(requests.get("https://api.meetup.com/find/groups?zip=97215&category="+str(cat)+"&key="+api_key).content.decode('utf-8'))))
# concatenate the dfs within cats_pdx_requests - need to automate
cats_pdx_df = pd.concat(cats_pdx_requests)

# resource: https://www.dataquest.io/blog/python-api-tutorial/
# alternate way perform request, using params= as argument for requests.get()
# seems to return a 'Response' type
response2 = requests.get("http://api.meetup.com/find/groups", params={'city':'Portland','category':34,'key':api_key})

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
cat1_pdx_df.count()
cat1_pdx_df.groupby('category.id').count()

# data check on multiple cat output
type(cats_pdx_df)
cats_pdx_df.head()
cats_pdx_df.count()
cats_pdx_df.groupby('category.id').count()


# filter dataframe for relevant categories
filtered_cats_pdx_df = cats_pdx_df[cats_pdx_df['category.id'].isin(example_mj_cats)]
filtered_cats_pdx_df.groupby('category.id').count()
