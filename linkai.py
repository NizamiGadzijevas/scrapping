from bs4 import BeautifulSoup
import requests
import re

source = requests.get('https://www.cvbankas.lt/?page=1').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('article', class_="list_article list_article_rememberable jobadlist_list_article_rememberable jobadlist_article_vip")
# print(blokai)
for blokas in blokai:
    try:
        linkas = blokas.find('a', class_="list_a can_visited list_a_has_logo")['href']
        # print(blokai)
        print(linkas)
    except:
        pass