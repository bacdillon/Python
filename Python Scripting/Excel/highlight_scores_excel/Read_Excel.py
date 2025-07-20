import pandas as pd

df = pd.read_excel('input_data.xlsx', sheet_name='Scores')
print(df.head())  # Show first 5 rows
