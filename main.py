import pandas as pd 
df = pd.read_csv("Features data set.csv")
columns_and_dtypes = list(zip(df.columns,df.dtypes))
for column,dtype in columns_and_dtypes:
    print(f"{column} {dtype}")
