import pandas as pd
import numpy as np

def ordinal_encoder(df):
  file=df.select_dtypes(include='object')
  new_file=pd.DataFrame()
  l=[]
  dict={}
  #ask for user preference
  print('Enter your choice:   1. Alphabetically   2. Random')
  k=int(input())

  for col in file.columns:

    if k==2:
      l=list(set(file[col].dropna()))
    elif k==1:
      l=sorted(file[col].dropna().unique())
    else:
      print("Enter valid value")
      ordinal_encoder(df)  
    #Create a dictionary of element present inside list with its index i as key
    for i in l:
      dict[i]= l.index(i)
    # Gives NaN value -1
    dict[np.nan]=-1  
  print(dict)
  #Changes the original column for encoded values
  for col in file.columns:
    new_file[col]= file[col].map(dict) 
    # Replace missing value with -1
    file[col] = file[col].fillna(-1)
  return new_file   

data = {
    'Age': [25, 30, np.nan, 22, 25, 28],
    'Salary': [50000, 60000, 60000, np.nan, 50000, 58000],
    'City': ['Delhi', 'Mumbai', np.nan, 'Delhi', 'Pune', np.nan],
    'Name': ['A','B','C','D','E','F']
}

df = pd.DataFrame(data)
k=ordinal_encoder(df)
print(k)
  