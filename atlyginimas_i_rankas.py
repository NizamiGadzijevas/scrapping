from bs4 import BeautifulSoup
import requests

# page = input(f"įveskitę sumą: ")
# url = f"https://cvkodas.lt/atlyginimo-skaiciuokle?gross={page}"
url = f"https://cvkodas.lt/atlyginimo-skaiciuokle?gross=2300"
pages = requests.get(url).text
soup = BeautifulSoup(pages, "html.parser")
blokai = soup.find('body')
print(blokai)
    # neto = blokai.find("span").text
    # # print(blokai)
    # print(neto)
