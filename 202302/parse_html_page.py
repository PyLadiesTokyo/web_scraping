from bs4 import BeautifulSoup  # ①

html = open('pyladies-top.html').read()  # ②
soup = BeautifulSoup(html, 'html.parser')  # ③
records = soup.find_all('a')

# for record in records:
#     print(record)

# for record in records:
#     if record.img:
#         continue
#     print(record)

# for record in records:
#     if record.img:
#         continue
#     #print(f'{record.string}: {record["href"]}')
#     print('{title}: {url}'.format(title=record.string, url=record["href"]))

with open('pyladies-staff.csv', 'w') as fout:
    for record in records:
        if record.img:
            continue
        fout.write(f'{record.string},{record["href"]}\n')