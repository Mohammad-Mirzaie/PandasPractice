# How do I apply multiple filter criteria to a pandas DataFrame?
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()

#multiple cretiria
movies[(movies.duration >=200) & (movies.star_rating <=8)]
# multiple filtering criteria and showing specific columns using LOC
movies.loc[(movies.duration >=200) & (movies.star_rating <=8), ['title','star_rating', 'duration']]



