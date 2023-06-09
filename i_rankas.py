import pandas as pd
import numpy as np

data = pd.read_csv('cvbankas.csv', encoding="utf-8")

ATLYGINIMAS_NUO = data['ATLYGINIMAS_NUO']
Socialinio_draudimo_mokesciai = ATLYGINIMAS_NUO * 0.0199 + ATLYGINIMAS_NUO * 0.0698

NPD = np.where(ATLYGINIMAS_NUO <= 625, ATLYGINIMAS_NUO,
               np.where(ATLYGINIMAS_NUO <= 840, 625,
                        np.where(ATLYGINIMAS_NUO <= 1926, 625 - 0.42 * (ATLYGINIMAS_NUO - 840),
                                 np.where(ATLYGINIMAS_NUO <= 2864.22, 400 - 0.18 * (ATLYGINIMAS_NUO - 642), 0))))

Gyventojų_pajamų_mokestis = (ATLYGINIMAS_NUO - NPD) * 0.2

mokesciai = round(Socialinio_draudimo_mokesciai + NPD + Gyventojų_pajamų_mokestis, 2)
print(mokesciai)
data.loc[data['APMOKĖJIMO_BŪDAS'] == 'Neatskaičius mokesčių', 'ATLYGINIMAS_NUO'] -= mokesciai

ATLYGINIMAS_IKI = data['ATLYGINIMAS_IKI']
Socialinio_draudimo_mokesciai = ATLYGINIMAS_IKI * 0.0199 + ATLYGINIMAS_IKI * 0.0698

NPD = np.where(ATLYGINIMAS_IKI <= 625, ATLYGINIMAS_IKI,
               np.where(ATLYGINIMAS_IKI <= 840, 625,
                        np.where(ATLYGINIMAS_IKI <= 1926, 625 - 0.42 * (ATLYGINIMAS_IKI - 840),
                                 np.where(ATLYGINIMAS_IKI <= 2864.22, 400 - 0.18 * (ATLYGINIMAS_IKI - 642), 0))))

Gyventojų_pajamų_mokestis = (ATLYGINIMAS_IKI - NPD) * 0.2

mokesciai = round(Socialinio_draudimo_mokesciai + NPD + Gyventojų_pajamų_mokestis, 2)
data.loc[data['APMOKĖJIMO_BŪDAS'] == 'Neatskaičius mokesčių', 'ATLYGINIMAS_IKI'] -= mokesciai
data.loc[data['APMOKĖJIMO_BŪDAS'] == 'Neatskaičius mokesčių', 'APMOKĖJIMO_BŪDAS'] = "Į rankas"

data.to_csv('updated_file.csv', index=False)
# print(data)
