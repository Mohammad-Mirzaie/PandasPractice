import pandas as pd

# read csv file
ufo = pd.read_csv("http://bit.ly/uforeports")

#show data type
print(type(ufo['City']))


print(ufo['Colors Reported'])

#Add a series 
ufo['Location'] = ufo.City + ', ' + ufo.State
print(ufo.head())
