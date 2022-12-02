#How do I filter rows of a pandas DataFrame by column value?
#There are two method:
# methode 1 is using for loop
# method 2 is shorter and commonly used

import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()
movies.shape

# 1. Filter pandas dataframe using for loop
booleans = []
for length in movies.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)

# show list
booleans[0:5]
# show length of list
len(booleans)

# convert list to Pandas series
is_long = pd.Series(booleans)
is_long.head()

# 2. better and more common method to filter pandas dataframe
#--------------------------------------------------------------------------
isLong = movies.duration >= 200
movies[isLong]

# We can write condition directly into brackets
# movies[condition]
movies[movies.duration >= 200]

# Filter dataframe and pull only some  columns
movies[movies.duration >= 200].genre
#or
movies[movies.duration >= 200]['genre']

# Multiple condition
movies[(movies.duration >= 150) & (movies.star_rating <= 8)]

# ------------------------------------------------------------------------------------
# best practice for filtering rows in a dataframe: USING LOC
# ------------------------------------------------------------------------------------

# dataframe_name.loc[condition, ['col1', 'col2', 'col3']]
movies.loc[movies.duration >= 200, ['genre','title']]