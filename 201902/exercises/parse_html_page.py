from bs4 import BeautifulSoup  # ①

html = open('pyladies-locations.html').read()  # ②
soup = BeautifulSoup(html, 'html.parser')  # ③
records = soup.find_all('div', class_="chapter_location")
print('加盟数=', len(records))
for record in records:
    a_tags = record.find_all('a')
    # 先頭のaタグの情報を表示
    print(record.a.string.strip(), end='\t')
    if 'http' in record.a['href']:
        print(record.a['href'], end='\t')
    else:
        print('\t', end='')
    # twitter情報があれば表示
    a_twitter = record.find('a', class_='social icon twitter')
    if a_twitter:
        print(a_twitter['href'])
    else:
        # 改行のみ
        print('')
