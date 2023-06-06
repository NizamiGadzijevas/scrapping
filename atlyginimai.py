import requests
from bs4 import BeautifulSoup
import re

page = requests.get("https://www.cvbankas.lt/?page=1").text
doc = BeautifulSoup(page, "html.parser")
numeriai = doc.find('ul', class_="pages_ul_inner")
nr = int(numeriai.find_all('a', )[-1].text)
# print(nr)


for page in range(1, 1 + 1):
    url = f"https://www.cvbankas.lt/?page={page}"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    blokai = soup.find_all('a', class_='list_a can_visited list_a_has_logo')

    for blokas in blokai:
        try:
            atlyginimas = blokas.find('span', class_="salary_amount").text
            apmokejimo_periodiskumas = blokas.find('span', class_="salary_period").text
            apmokejimo_budas = blokas.find('span', class_="salary_calculation").text
            if '-' in atlyginimas:
                atl = atlyginimas.split('-')
                atl_nuo = atl[0]
                atl_iki = atl[1]
                print(atl_nuo + " " + apmokejimo_periodiskumas, apmokejimo_budas)
                print(atl_iki + " " + apmokejimo_periodiskumas, apmokejimo_budas)
            elif "Nuo" in atlyginimas:
                print(atlyginimas[4:] + apmokejimo_periodiskumas, apmokejimo_budas)
            else:
                print(atlyginimas + apmokejimo_periodiskumas, apmokejimo_budas)
            # atl = atlyginimas.split()
            # atl_nuo = atl[0]
            # atl_iki = atl[1]
            # print(atl)
            # print(atl_nuo, atl_iki)
            # print(atlyginimas)

        except:
            pass
