# scraper.py
import requests
from bs4 import BeautifulSoup


def get_text(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'lxml')
    txt = soup.find('div', id='entry')
    return txt.p.text



zodiacs = ['Рыбы', 'Водолей', 'Козерог', 'Стрелец', 'Скорпион', 'Весы', 'Дева', 'Лев', 'Рак', 'Близнецы', 'Телец',
           'Овен']
exceptions = ['Водоле', 'Тельц', 'Рыб', 'Козерог', 'Стрель', 'Скорпион', 'Вес', 'Девам', 'Льв', 'Рак', 'Близнец',
              'Овнам']

with open(r'C:\Users\ugl\Desktop\iwannapars\result.txt', 'a', encoding="utf-8") as file:
    url = 'https://mygazeta.com/category/гороскоп/'
    for _ in range(500):
        resp = requests.get(url)
        sup = BeautifulSoup(resp.text, 'lxml')
        titles = sup.find_all('h2', class_='archiveTitles')
        zodiac_counter = 0

        for lnk in titles:
            flag = 1
            text = get_text(lnk.find("a")["href"]).strip().replace("&nbsp", "")
            for exception in exceptions:
                if exception in text:
                    flag = 0
                    break
            if flag:
                file.write(f'[START]{zodiacs[zodiac_counter]}:{text}[END]\n')
            zodiac_counter += 1

        url = sup.find('a', class_="page larger")["href"]
