from bs4 import BeautifulSoup

html = open('pyladies-top.html', encoding='utf8').read()
soup = BeautifulSoup(html, 'html.parser')

records = soup.find_all('a')
for record in records:
    if record.img:
        continue

    # PyLadies Tokyo: https://pyladiestokyo.github.io
    print(f'{record.text}: {record["href"]}')

