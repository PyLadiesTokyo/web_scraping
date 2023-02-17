import requests
from bs4 import BeautifulSoup

res = requests.get('https://pyladies.com/locations/')
soup = BeautifulSoup(res.content, "html.parser")

locations = soup.find_all('div', class_='chapter_location')

for location in locations:
    name = location.find('h3', class_='chpts chapter-name').text.strip()
    mail = location.find('h3', class_='chpts social-icons').find('a', class_='icon-mail4')

    print(f'{name}: {mail["href"].removeprefix("mailto:")}')


