import pandas as pd
import numpy as np


data = pd.read_csv('cvbankas.csv', encoding="utf-8")

if ATLYGINIMAS_NUO <= 625:
    NPD = ATLYGINIMAS_NUO
if ATLYGINIMAS_NUO > 625 or ATLYGINIMAS_NUO <= 840:
    NPD = 625
if ATLYGINIMAS_NUO > 840 or ATLYGINIMAS_NUO <= 1926:
    NPD = 625-0.42*(ATLYGINIMAS_NUO - 840)
if ATLYGINIMAS_NUO > 1926 or ATLYGINIMAS_NUO <= 2864.22:
    NPD = 400-0.18*(ATLYGINIMAS_NUO-642)
else:
    NPD = 0
mokesciai = Socialinio_draudimo_mokesciai + NPD + Gyventojų_pajamų_mokestis
Socialinio_draudimo_mokesciai = ATLYGINIMAS_NUO * 0.0199 + ATLYGINIMAS_NUO * 0.0698

Gyventojų_pajamų_mokestis = (ATLYGINIMAS_NUO-NPD)*0.2
# Gyventojų_pajamų_mokestis = round(ATLYGINIMAS_NUO-NPD)*0.2 , 2))

mokesciai = Socialinio_draudimo_mokesciai + NPD + Gyventojų_pajamų_mokestis

data.loc[(data.APMOKĖJIMO_PERIODIŠKUMAS == 'Neatskaičius mokesčių'),'ATLYGINIMAS_NUO'] -= mokesciai
data.loc[(data.APMOKĖJIMO_PERIODIŠKUMAS == 'Neatskaičius mokesčių'),'ATLYGINIMAS_IKI'] -= mokesciai
data.to_csv('updated_file.csv', index=False)
print(data)