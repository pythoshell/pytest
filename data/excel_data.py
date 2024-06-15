import pandas as pd
import os

# Get the current working directory
current_directory = os.getcwd()
print(current_directory)

#encoding = result['encoding']
df = pd.read_csv("C:\pyauto\pytest\data\datacsv.csv",encoding='latin1')
print(df.tail())
c = df.columns
print(c)
