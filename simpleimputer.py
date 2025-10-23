import pandas as pd
import numpy as np

def simple_imputer(X_train):

  file=X_train.copy()
  # Ask for user preference
  strtgy=int(input("Enter Strategy: \n 1. mean  2. median  3. most frequent  4. constant\n"))

  # for mean
  
  if strtgy==1:
   file= file.select_dtypes(exclude='object')
   for cl in file.columns:
     file.loc[file[cl].isnull(), cl] = file[cl].mean()
   return file
  
  # for median

  elif strtgy==2:
   file= file.select_dtypes(exclude='object')
   for cl in file.columns:
     file.loc[file[cl].isnull(), cl] = file[cl].median()
   return file 
  
  # for most frequent
  
  elif strtgy==3:
   for cl in file.columns:
     file.loc[file[cl].isnull(), cl] = file[cl].mode()[0]
   return file 
  
  # for constant

  elif strtgy==4:
   c_n=input("Enter numerical constant: ")
   c_c=input("Enter categorical constant: ")
   for cl in file.columns:
     if cl in file.select_dtypes(exclude='object'):
       file.loc[file[cl].isnull(), cl]=c_n
     else:
       file.loc[file[cl].isnull(), cl]=c_c 
   return file 
  
  else:
    print("Enter a valid strategy")
    simple_imputer(df)

data = {
    'Age': [25, 30, np.nan, 22, np.nan, 28],
    'Salary': [50000, np.nan, 60000, 52000, np.nan, 58000],
    'City': ['Delhi', 'Mumbai', np.nan, 'Delhi', 'Pune', np.nan]
}

df = pd.DataFrame(data)
k=simple_imputer(df)
print(k)