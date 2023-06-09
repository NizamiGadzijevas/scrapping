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
    blokai = soup.find('div', id="js_id_id_job_ad_list")
    miestai = blokai.find_all('span', class_="txt_list_1")
    print(miestai)
    # print(blokai)
    for blokas in miestai:
        try:
            miestas = blokas.find('span', class_="list_city").get_text
            print(miestas)

        except:
            pass
