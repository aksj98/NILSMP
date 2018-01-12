import pandas as pd

#reading the file
df = pd.read_csv('data.csv')

#cleaning the data
df.drop(['Series','Symbol','Low Price','Last Price', 'Prev Close', 'Average Price','Total Traded Quantity','No. of Trades','Deliverable Qty','Close Price'], axis=1, inplace=True)

#df now contains only the required data

