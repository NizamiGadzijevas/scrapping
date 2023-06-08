import pandas as pd

#create DataFrame
data = pd.read_csv('cvbankas.csv', encoding="utf-8")

data.loc[(data.APMOKĖJIMO_PERIODIŠKUMAS == '€/val.'),'ATLYGINIMAS_NUO']*=8
data.to_csv('updated_file.csv', index=False)  # Replace 'updated_file.csv' with the desired file name
print(data)

#view DataFrame
# df['ATLYGINIMAS NUO'] = df['APMOKĖJIMO BŪDAS'].map(lambda x: 'Atlanta' if '€/val.' in x else 'Boston' if 'B' in x else 'testas')
# print(df)
