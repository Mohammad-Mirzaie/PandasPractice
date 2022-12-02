#Why do some pandas commands end with parentheses (and others don't)?

import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
print(movies.head())
#pandas's command end with parentheses is method
movies.describe(include=['object'])
#pandas's command end without parentheses is atribute
movies.shape
movies.dtypes
type(movies)


