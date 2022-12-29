import pandas as pd
df_csv=pd.read_csv('pokemon_data.csv')
#df_csv['oddsum']=df_csv.iloc[1::2,[5,6,9]].sum(axis=1)
a=df_csv.loc[df_csv['Name'].str.startswith('A')]
#print(a)
print((df_csv.groupby(['Type 1']).sum()).to_string())
#df_csv['#']=pd.date_range("20010101",periods=800)
#print(df_csv)