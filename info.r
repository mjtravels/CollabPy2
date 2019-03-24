# Note: This is formatted for logging into different servers in R
# To convert to Python, change to dict format

logins = list(
  'source1' = data.frame(username = 'example'
                         , password = 'example'
                         , stringsAsFactors = FALSE)
  , 'source1' = data.frame(username = 'example'
                            , password = 'example'
                            , stringsAsFactors = FALSE)
)

#to use in RStudio:
#1) copy to local directory
#2) run following:
#		source('[path]/info.R')
#3) run to set up driver and connection:
#		login <- logins[['[source1/source2]']]
