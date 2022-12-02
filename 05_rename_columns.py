#How do I rename columns in a pandas DataFrame?
# replace white space with under score



import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head()
#shows list of column names
ufo.columns
#rename columns
ufo.rename(columns={'Colors Reported':'Colors_Reported', 'Shape Reported':'Shaped_Reported'}, inplace=True)
ufo.columns

#rename columns
#first create a python list
ufo_cols =['city', 'colors_reported', 'shape_reported', 'state', 'time']
#rename ufo columns using above list
ufo.columns = ufo_cols
ufo.head()

# renaming columns while reading csv file
ufo = pd.read_csv('http://bit.ly/uforeports', names=ufo_cols, header=0)
ufo.head()


#How to replace white spaces with under score
ufo.columns=ufo.columns.str.replace(" ", "_")
ufo.columns