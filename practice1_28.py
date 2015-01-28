from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# IMPORTING DATA--------------------------
## assigning file paths
main_dir="/Users/tigents/Documents/Big-Data" 
csv_file = "/data/sample_data_clean.csv"
txt_file = "/data/sample_data_clean.txt"

main_dir + csv_file
main_dir + txt_file

# read_csv and read_table
df = pd.read_csv(main_dir + csv_file)
df2 = pd.read_table(main_dir + txt_file)

## check type
type(df)

# EXPLORING DATA
list(df)

# extracting data
c=df.consump
c2=df['consump']

##Boolean (logic) operators
c == c2
c>c2
c!=c2

#row extraction
df[5:10]
df.consump[5:10]

#extracting by boolean indexing
df[df.panid==4]
df[df.consump>2]