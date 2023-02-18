import requests
from bs4 import BeautifulSoup

# クローリングする
# res = requests.get('https://www.pyladies.com/locations/')
# with open('location.html', 'wb') as fout:
#     fout.write(res.content)

# beautifulsoupに解析させる
html = open('location.html', encoding='utf8').read()
soup = BeautifulSoup(html, 'html.parser')

# 欲しいデータを抽出する・整形する
locations = soup.find_all('div', class_='chapter_location')

with open('contact.txt', 'w', encoding='utf8') as fout:
    for location in locations:
        # 都市名を取得
        name = location.find('h3', class_='chpts chapter-name')
        # print(name.text.strip())

        # メールアドレスを取得
        address = location.find('a', class_='icon-mail4')
        # print(address["href"].removeprefix("mailto:"))
        if address is None:
            mail = "メールアドレスはありません"
        else:
            mail = address["href"].removeprefix("mailto:")

        # 整形する
        fout.write(f'{name.text.strip()}: {mail}\n')
