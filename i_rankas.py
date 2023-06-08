import pandas as pd

#create DataFrame
data = pd.read_csv('testas.csv', encoding="utf-8")

data.loc[(data.apmokejimas == '€/val.'),'atlyginimas']*=8
data.to_csv('updated_file.csv', index=False)  # Replace 'updated_file.csv' with the desired file name
print(data)

#view DataFrame
# df['ATLYGINIMAS NUO'] = df['APMOKĖJIMO BŪDAS'].map(lambda x: 'Atlanta' if '€/val.' in x else 'Boston' if 'B' in x else 'testas')
# print(df)
