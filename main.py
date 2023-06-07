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
                pareigos = blokas.find('h3', class_="list_h3").text.strip()
                imone = blokas.find('span', class_="dib mt5").text.strip()
                linkas = blokas.find('a', class_="list_a can_visited list_a_has_logo")['href']
                print(atlyginimas, pareigos, imone, linkas)
            except:
                pass
