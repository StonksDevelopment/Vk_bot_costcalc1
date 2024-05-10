import requests
from bs4 import BeautifulSoup

URL = "https://www.banki.ru/products/currency/cny/"

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        print("Ответ получен")
        soup = BeautifulSoup(html.text, "html.parser")
        item = soup.find("div",class_="currency-table__large-text").text
        print(item)
    else:
        print("Ответ не получен.")

def get_html(url):
    r = requests.get(url)
    return r

parse()