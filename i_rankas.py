import pandas as pd

data = pd.read_csv('cvbankas.csv', encoding="utf-8")

# ATLYGINIMAS_NUO = 2000
ATLYGINIMAS_NUO = data['ATLYGINIMAS_NUO']
Socialinio_draudimo_mokesciai = ATLYGINIMAS_NUO * 0.0199 + ATLYGINIMAS_NUO * 0.0698

if ATLYGINIMAS_NUO <= 625:
    NPD = ATLYGINIMAS_NUO
elif ATLYGINIMAS_NUO <= 840:
    NPD = 625
elif ATLYGINIMAS_NUO <= 1926:
    NPD = 625 - 0.42 * (ATLYGINIMAS_NUO - 840)
elif ATLYGINIMAS_NUO <= 2864.22:
    NPD = 400 - 0.18 * (ATLYGINIMAS_NUO - 642)
else:
    NPD = 0

Gyventoju_pajamu_mokestis = (ATLYGINIMAS_NUO - NPD) * 0.2

mokesciai = Socialinio_draudimo_mokesciai + NPD + Gyventoju_pajamu_mokestis
print(mokesciai)
data.loc[data['APMOKĖJIMO_BŪDAS'] == 'Neatskaicius mokescius', 'ATLYGINIMAS_NUO'] -= mokesciai
data.loc[data['APMOKĖJIMO_BŪDAS'] == 'Neatskaicius mokescius', 'ATLYGINIMAS_IKI'] -= mokesciai

data.to_csv('updated_file.csv', index=False)
print(data)
