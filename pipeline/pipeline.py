import sys
import pandas as pd

print('Arguments:', sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"Day": [1, 2], "Passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f'output_{month}.parquet')    

print(f'Hello pipeline, month={month}')