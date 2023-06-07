from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.cvbankas.lt/?page=1').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('article', class_="list_article list_article_rememberable jobadlist_list_article_rememberable jobadlist_article_vip")
# print(blokai)
for blokas in blokai:
    try:
        linkas = blokas.find('a', class_="list_a can_visited list_a_has_logo")['href']
        skelbimas = requests.get(linkas).text
        soup = BeautifulSoup(skelbimas, 'html.parser')
        reikalavimai = soup.find('h2', class_="heading2 jobad_subheading").get_text()

        # print(blokai)
        # print(linkas)
        print(reikalavimai)
    except:
        pass