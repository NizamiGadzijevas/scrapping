import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.cvbankas.lt/?page=1").text
doc = BeautifulSoup(page, "html.parser")
numeriai = doc.find('ul', class_="pages_ul_inner")
nr = int(numeriai.find_all('a', )[-1].text
profesijos = input(f"Įveskite profesiją:/n")
# print(nr)


for page in range(1, 1 + 1):
    url = f"https://www.cvbankas.lt/?page={page}"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    blokai = soup.find_all('article', class_="list_article list_article_rememberable jobadlist_list_article_rememberable jobadlist_article_vip")

    for blokas in blokai:
        try:
            profesija = blokas.find('div', class_="list_cell").text
            print(profesija)

        except:
            pass
