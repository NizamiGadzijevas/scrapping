import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://www.cvbankas.lt/?page=1").text
doc = BeautifulSoup(page, "html.parser")
numeriai = doc.find('ul', class_="pages_ul_inner")
nr = int(numeriai.find_all('a', )[-1].text)
# print(nr)

with open("cvbankas.csv", 'w', encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Pareigos', 'Atlyginimas', 'Įmonė', 'Nuoroda'])

    for page in range(1, 1 + 1):
        url = f"https://www.cvbankas.lt/?page={page}"
        page = requests.get(url).text
        soup = BeautifulSoup(page, "html.parser")
        blokai = soup.find_all('article', class_="list_article list_article_rememberable jobadlist_list_article_rememberable jobadlist_article_vip")

        for blokas in blokai:
            try:
                atlyginimas = blokas.find('span', class_="salary_amount").text
                apmokejimo_periodiskumas = blokas.find('span', class_="salary_period").text
                apmokejimo_budas = blokas.find('span', class_="salary_calculation").text
                linkas = blokas.find('a', class_="list_a can_visited list_a_has_logo")['href']
                miestas = blokas.find('span', class_="list_city").text
                profesija = blokas.find('div', class_="list_cell").text
                # print(profesija)
                if '-' in atlyginimas:
                    atl = atlyginimas.split('-')
                    atl_nuo = atl[0]
                    atl_iki = atl[1]
                    # print(atl_nuo,atl_iki)
                elif "Nuo" in atlyginimas:
                    atl_nuo = atlyginimas[4:]
                    atl_iki = atlyginimas[4:]
                    # print(atl_nuo,atl_iki)

                else:
                    atl_nuo = atlyginimas
                    atl_iki = atlyginimas
                    # print(atl_nuo,atl_iki)

                # csv_writer.writerow([profesija, atl_nuo, atl_iki, apapmokejimo_budas, apmokejimo_periodiskumas, linkas])
                print(atl_nuo, atl_iki, apmokejimo_budas,apmokejimo_periodiskumas, linkas)

            except:
                pass
