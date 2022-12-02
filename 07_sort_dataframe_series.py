#How do I sort a pandas DataFrame or a Series?
import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()

#sort title values
movies.title.sort_values()
#or
movies['title'].sort_values(ascending=False)
#below command also sort by title but return all dataframe
movies.sort_values('title', ascending=False)

#sort by multiple columns
movies.sort_values(['content_rating', 'duration'])
movies.columns