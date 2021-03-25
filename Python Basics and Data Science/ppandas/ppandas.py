# Do not name this to pd.py or pandas.py to avoid errors
# pandas is a pre-written library for data analysis
# standard abbreviation pd

#import pandas as pd 

# csv is a typical store data type file
#csv_path="file1.csv"

# Importing from csv file to dataframe
#df=pandas.csv_path(csv_path)
#df=pd.read_csv(csv_path) # df = dataframe 
#df.head()

# Importing from an excel file to dataframe
#xlsx_path="file1.xlsx" 
#df=pd.read_excel(xlsx_path)
#df.head()

songs = {"Album":["Thriller","Back in Black", "The Dark Side of the Moon",\
         "The Bodyguard","Bat Out of Hell"],
         "Released":[1982,1980,1973,1992,1977],
         "Length":["00:42:19","00:42:11","00:42:49","00:57:44","00:46:33"]}
# Casting the dictionary to dataframe 
#songs_frame = pd.DataFrame(songs)
import pandas as pd 
df=pd.DataFrame(songs)
df.head(3)

# Create a new dataframe with only one column
#df[["Length"]]

# Create a new dataframe with multiples column
#df[["Album","Released","Length"]]

# Using method unique to find all unique elements
#df["Released"].unique()

# Using inequality operators to find elements and save the result to df1
#df1 = df["Released"]>=1980

# Save as CSV
#df1.to_csv("C:/Users/V/Desktop/pandas")

# Using IX method to access specific row snd specific column
#df.ix[0,0]
#df.ix[2,"Album"]
#df.iloc[1,0]

# another examples
#df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})
#df.head(3)
#df.iloc[0,1]





