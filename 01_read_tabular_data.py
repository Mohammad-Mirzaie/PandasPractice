import pandas as pd

#read_table function will read Tab Seperated file.
orders = pd.read_table('http://bit.ly/chiporders')
print(orders.head())
#----------------------------------------------------------------------------------------------
#below list will be used to be column's name 
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']

#sep='|' means seperator is pip not comma or tab 
#header=None means this dataset does not have any heading column
#name=user_cols means column's names will be the user_cols list
users = pd.read_table('http://bit.ly/movieusers', sep='|', header=None, names=user_cols)
print(users.head())
