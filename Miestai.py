import requests
from bs4 import BeautifulSoup


page = requests.get("https://www.cvbankas.lt/?page=1").text
doc = BeautifulSoup(page, "html.parser")
numeriai = doc.find('ul', class_="pages_ul_inner")
nr = int(numeriai.find_all('a', )[-1].text)
# print(nr)


for page in range(1, 1 + 1):
    url = f"https://www.cvbankas.lt/?page={page}"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    blokai = soup.find_all('article', class_="list_article list_article_rememberable jobadlist_list_article_rememberable jobadlist_article_vip")
    # print(blokai)
    for blokas in blokai:
        try:
            miestas = blokas.find('span', class_="list_city").text
            print(miestas)

        except:
            pass
