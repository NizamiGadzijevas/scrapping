import time
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import numpy as np


page = requests.get("https://www.cvbankas.lt/?page=1").text
doc = BeautifulSoup(page, "html.parser")
numeriai = doc.find('ul', class_="pages_ul_inner")
nr = int(numeriai.find_all('a', )[-1].text)
# print(nr)

with open("cvbankas.csv", 'w', encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['PROFESIJA','MIESTAS', 'ATLYGINIMAS_NUO', 'ATLYGINIMAS_IKI', 'APMOKĖJIMO_PERIODIŠKUMAS', 'APMOKĖJIMO_BŪDAS', 'ĮMONĖ', 'Nuoroda'])

    for page in range(1, nr + 1):
        url = f"https://www.cvbankas.lt/?page={page}"
        page = requests.get(url).text
        soup = BeautifulSoup(page, "html.parser")
        # blokai = soup.find_all('article', class_="list_article list_article_rememberable jobadlist_list_article_rememberable")
        # blokai = soup.find_all('article', class_="list_article list_article_rememberable jobadlist_list_article_rememberable jobadlist_article_vip")
        blokai = soup.find('div', id="js_id_id_job_ad_list")
        time.sleep(4)

        for blokas in blokai:
            try:
                atlyginimas = blokas.find('span', class_="salary_amount").text
                apmokejimo_periodiskumas = blokas.find('span', class_="salary_period").text
                apmokejimo_budas = blokas.find('span', class_="salary_calculation").text
                linkas = blokas.find('a', class_="list_a can_visited list_a_has_logo")['href']
                miestas = blokas.find('span', class_="list_city").text
                profesija = blokas.find('h3', class_="list_h3").text
                # print(profesija)
                if '-' in atlyginimas:
                    atl = atlyginimas.split('-')
                    atl_nuo = float(atl[0])
                    atl_iki = float(atl[1])
                    # print(atl_nuo,atl_iki)
                    # print(type(atl_nuo))

                    # print(type(atl_nuo))
                elif "Nuo" in atlyginimas:
                    atl_nuo = float(atlyginimas[4:])
                    atl_iki = float(atlyginimas[4:])
                    # print(atl_nuo,atl_iki)

                else:
                    atl_nuo = float(atlyginimas)
                    atl_iki = float(atlyginimas)
                    # print(atl_nuo,atl_iki)

                csv_writer.writerow([profesija,miestas, atl_nuo, atl_iki,apmokejimo_periodiskumas, apmokejimo_budas, linkas])
                print(profesija,miestas, atl_nuo, atl_iki, apmokejimo_budas, apmokejimo_periodiskumas, linkas)

            except:
                pass

data = pd.read_csv('cvbankas.csv', encoding="utf-8")
data.loc[data['APMOKĖJIMO_PERIODIŠKUMAS'] == '€/val.','ATLYGINIMAS_NUO']*=160
data.loc[data['APMOKĖJIMO_PERIODIŠKUMAS'] == '€/val.','ATLYGINIMAS_IKI']*=160
data.loc[data['APMOKĖJIMO_PERIODIŠKUMAS'] == '€/val.','APMOKĖJIMO_PERIODIŠKUMAS'] = "€/mėn."
data.to_csv('updated_file.csv', index=False)


ATLYGINIMAS_NUO = data['ATLYGINIMAS_NUO']
Socialinio_draudimo_mokesciai = ATLYGINIMAS_NUO * 0.0199 + ATLYGINIMAS_NUO * 0.0698

NPD = np.where(ATLYGINIMAS_NUO <= 625, ATLYGINIMAS_NUO,
               np.where(ATLYGINIMAS_NUO <= 840, 625,
                        np.where(ATLYGINIMAS_NUO <= 1926, 625 - 0.42 * (ATLYGINIMAS_NUO - 840),
                                 np.where(ATLYGINIMAS_NUO <= 2864.22, 400 - 0.18 * (ATLYGINIMAS_NUO - 642), 0))))

Gyventojų_pajamų_mokestis = (ATLYGINIMAS_NUO - NPD) * 0.2

mokesciai = round(Socialinio_draudimo_mokesciai + Gyventojų_pajamų_mokestis, 2)
data.loc[data['APMOKĖJIMO_BŪDAS'] == 'Neatskaičius mokesčių', 'ATLYGINIMAS_NUO'] -= mokesciai

ATLYGINIMAS_IKI = data['ATLYGINIMAS_IKI']
Socialinio_draudimo_mokesciai = ATLYGINIMAS_IKI * 0.0199 + ATLYGINIMAS_IKI * 0.0698

NPD = np.where(ATLYGINIMAS_IKI <= 625, ATLYGINIMAS_IKI,
               np.where(ATLYGINIMAS_IKI <= 840, 625,
                        np.where(ATLYGINIMAS_IKI <= 1926, 625 - 0.42 * (ATLYGINIMAS_IKI - 840),
                                 np.where(ATLYGINIMAS_IKI <= 2864.22, 400 - 0.18 * (ATLYGINIMAS_IKI - 642), 0))))

Gyventojų_pajamų_mokestis = (ATLYGINIMAS_IKI - NPD) * 0.2

mokesciai = round(Socialinio_draudimo_mokesciai + Gyventojų_pajamų_mokestis, 2)
data.loc[data['APMOKĖJIMO_BŪDAS'] == 'Neatskaičius mokesčių', 'ATLYGINIMAS_IKI'] -= mokesciai
data.loc[data['APMOKĖJIMO_BŪDAS'] == 'Neatskaičius mokesčių', 'APMOKĖJIMO_BŪDAS'] = "Į rankas"

data.to_csv('updated_file.csv', index=False)

