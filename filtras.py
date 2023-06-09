import pandas as pd

data = pd.read_csv('updated_file.csv', encoding="utf-8")

profesija = input(f"Įveskite profesijos šaknį arba visą pavadinimą: \n")
miestas = input(f'Įveskite miestą naudininku, pvz.: Vilniuje: \n')
atlyginimas = int(input("Įveskite min atlyginimą: \n"))

filtras = data[(data['PROFESIJA'].str.contains(profesija, case=False)) &
               (data['MIESTAS'].str.contains(miestas, case=False)) &
               (data['ATLYGINIMAS_NUO'] > atlyginimas) &
               (data['ATLYGINIMAS_IKI'] > atlyginimas)]
print(filtras)
filtras.to_csv('filtras.csv', index=False)
