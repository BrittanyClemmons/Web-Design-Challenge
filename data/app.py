# import library
import pandas as pd

# Read in csv data
csv = pd.read_csv('cities.csv')
df = pd.DataFrame(csv)

# Verify that data is there
# print(df.head())

# Convert dataframe into html
csv.to_html('table.html', classes=['table', 'table-hover', 'thead-dark'])