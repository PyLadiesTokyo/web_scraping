# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

def converet_url_to_fanem(url):
    fname = url.replace('http://', '').replace('/', '#')
    return fname

def save_htmlfile(url, fname):
    res = requests.get(url)
    if res.status_code == 200:
        with open(fname, 'wb') as fout:
            fout.write(res.content)

def scrape_nihonshu_list_data(fname):
    html = open(fname).read()
    soup = BeautifulSoup(html, 'html.parser')
    # CSS情報を使ってデータを抜く
    records = soup.select('td')

    nihonshus = []
    links = []
    shuzos = []
    for record in records:
        if record.h2:
            links.append(record.a.get('href'))
            nihonshus.append(record.a.get_text())
            continue
        shuzos.append(record.string)
    return nihonshus, links, shuzos


def main():
    url = 'http://www.japan1000.com/sake/brand_list.php'
    fname = converet_url_to_fanem(url)
    save_htmlfile(url, fname)
    nihonshus, links, shuzos = scrape_nihonshu_list_data(fname)
    with open('nihonshu_list.csv', 'w') as fout:
        for nihonshu, link, shuzo in zip(nihonshus, links, shuzos):
            link = urljoin(url, link)
            fout.write('{nihonshu},{link},{shuzo}\n'.format(**locals()))

if __name__ == "__main__":
    main()
