import pandas as pd
import sys
import os
from datetime import date

# arg from applescript that gets the location of the xlsx file
fileloc = sys.argv[1]

# read the excel file
df = pd.read_excel(fileloc)

# strip unecessary columns and leaving whats needed
df = df[['DSM', 'Util %']]

# remove NaN's
df = df.dropna()    

# Removes any rows that have inapplicable data
df = df[(~df['DSM'].str.contains('ARCHIVE|INACTIVE|EXPIRED|CUST DEFERRED')) & (~df['Util %'].str.contains("NaN|Inactive"))]

# Sliced all objects in the 'Util %' column leaving only the first two characters
df['Util %'] = df['Util %'].str.slice(stop=2)
# Peaked Util was sliced to Pe and "Peaked Util" == 100
df['Util %'] = df['Util %'].replace("Pe", 100)

# Since all values in 'Util %' are integers, we can convert it to a int series
df['Util %'] = df['Util %'].astype(int)

# Create a new dataframe that groups by the DSM names and take the mean of each DSM utilization
newdf = df.groupby('DSM', as_index=False).mean()

# Rename the columns of the new dataframe
newdf.columns = ['DSM', 'AVG Util %']

# Retrieve today's date
date = date.today()

# Format the location of the new xlsx and its name + date
# Have to use old formatting method due to python 2.7 (Default MacOS Python ver.)
# cwdfinal = "%s/AVGUTIL %s.xlsx" % (fileloc1, date)

newdf.to_excel("AVGUTIL.xlsx", index=False)

# print for debugging
print('done!')
