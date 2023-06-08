import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


page = requests.get("https://www.cvbankas.lt/?page=1").text
doc = BeautifulSoup(page, "html.parser")
numeriai = doc.find('ul', class_="pages_ul_inner")
nr = int(numeriai.find_all('a', )[-1].text)
# print(nr)

with open("cvbankas.csv", 'w', encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['PROFESIJA', 'ATLYGINIMAS_NUO', 'ATLYGINIMAS_IKI', 'APMOKĖJIMO_PERIODIŠKUMAS', 'APMOKĖJIMO_BŪDAS', 'ĮMONĖ', 'Nuoroda'])

    # for page in range(1, 1 + 1):
    for page in range(1, 5 + 1):
        url = f"https://www.cvbankas.lt/?page={page}"
        page = requests.get(url).text
        soup = BeautifulSoup(page, "html.parser")
        # blokai = soup.find_all('article', class_="list_article list_article_rememberable jobadlist_list_article_rememberable")
        # blokai = soup.find_all('article', class_="list_article list_article_rememberable jobadlist_list_article_rememberable jobadlist_article_vip")
        blokai = soup.find('div', id="js_id_id_job_ad_list")

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

                csv_writer.writerow([profesija, atl_nuo, atl_iki,apmokejimo_periodiskumas, apmokejimo_budas, linkas])
                print(profesija, atl_nuo, atl_iki, apmokejimo_budas, apmokejimo_periodiskumas, linkas)

            except:
                pass
data = pd.read_csv('cvbankas.csv', encoding="utf-8")
data.loc[(data.APMOKĖJIMO_PERIODIŠKUMAS == '€/val.'),'ATLYGINIMAS_NUO']*=160
data.loc[(data.APMOKĖJIMO_PERIODIŠKUMAS == '€/val.'),'ATLYGINIMAS_IKI']*=160
data.to_csv('updated_file.csv', index=False)  # Replace 'updated_file.csv' with the desired file name