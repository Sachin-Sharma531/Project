import pandas as pd
import numpy as np

def OH_encoder(df):
  file=df.select_dtypes(include='object')
  for col in file.columns:
    s=file[col].dropna().unique()
    for i in s:
      file[i]= df[col]==i 
  file=file.select_dtypes(include=bool)
  return file




data = {
    'Age': [25, 30, np.nan, 22, np.nan, 28],
    'Salary': [50000, np.nan, 60000, 52000, np.nan, 58000],
    'City': ['Delhi', 'Mumbai', np.nan, 'Delhi', 'Pune', np.nan]
}

df = pd.DataFrame(data)
k=OH_encoder(df)
print(k)