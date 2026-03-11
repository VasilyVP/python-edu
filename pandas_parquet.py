import pandas as pd
import duckdb

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

df = pd.DataFrame(mydataset)

# Save the DataFrame to a Parquet file
df.to_parquet('mydataset.parquet')

# Read the Parquet file using pandas
#table = pd.read_parquet("mydataset.parquet")
#print(table.head())

# Read the Parquet file using duckdb
df = duckdb.query("SELECT * FROM 'mydataset.parquet'").to_df()
print(df.head(2))


