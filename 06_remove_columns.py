# How do I remove columns from a pandas DataFrame?
# How to remove rows?
import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()
ufo.shape

#remove column
#axis=1 means I want to drop columns. Below code means Colors Reported column will be deleted.
ufo.drop('Colors Reported', axis=1, inplace=True)
ufo.head()

#remove multiple columns
ufo.drop(['City', 'State'], axis=1, inplace=True)
ufo.head()

#remove row
# axis = 0 means row Default and we can dont write it.
# axis = 1 means column
ufo.drop([0, 1], axis=0, inplace= True)
ufo.head()
ufo.shape
