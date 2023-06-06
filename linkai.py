from bs4 import BeautifulSoup
import requests
import re

source = requests.get('https://www.cvbankas.lt/?page=1').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('a', class_="list_a can_visited list_a_has_logo")
# blokai = soup.find_all('a', class_=re.compile(r'list_a_has_logo'))
# blokas = blokai.find_all('a', class_=re.compile(r'list_a_has_logo'))['href']
# blokas = blokai.find('a', class_="list_a can_visited list_a_has_logo")['href']
print(blokai)
print(blokas)