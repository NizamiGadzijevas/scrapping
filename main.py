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
    blokai = soup.find_all('div', class_="list_a_wrapper")

    for blokas in blokai:
        try:
            atlyginimas = blokas.find('span', class_="salary_amount").text.strip()
    #         pareigos = blokas.find('h3', class_="list_h3").text.strip()
    #         imone = blokas.find('span', class_="dib mt5").text.strip()
    #         # nuoroda = blokas.find('a', class_="list_a can_visited list_a_has_logo")['href']
            print(atlyginimai)
            # print(atlyginimai, pareigos, imone)
    #         # csv_writer.writerow([pareigos, atlyginimas, imone])
    #         csv_writer.writerow(['Pareigos', 'Atlyginimas', 'Imone'])
    #
        except:
            pass
