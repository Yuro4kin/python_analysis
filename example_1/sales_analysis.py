import pandas as pd



# Task #1: Merging 12 csvs into a single dataframe
#  Read single CSV file
df = pd.read_csv("./Sales_Data/Sales_August_2019.csv")
print(df.head())