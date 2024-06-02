import pandas as pd

import os

# Get the current working directory
current_directory = os.getcwd()
print(current_directory)

excel_df = pd.read_csv('datacsv.csv')
print(excel_df.head())
