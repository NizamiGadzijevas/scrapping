import pandas as pd

data = pd.read_csv('updated_file.csv')

profesija = 'Vyr. buhalteris (-ė)'
miestas = 'Vilniuje'
atlyginimas = 1400

filtras = data[(data['PROFESIJA'] == profesija) & (data['MIESTAS'] == miestas) & (data['ATLYGINIMAS_NUO'] > atlyginimas)]

print(filtras)
