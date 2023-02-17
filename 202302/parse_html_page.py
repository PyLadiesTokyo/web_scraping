from bs4 import BeautifulSoup

html = open("pyladies-top.html", encoding="utf8").read()
soup = BeautifulSoup(html, "html.parser")

records = soup.find_all("a")
with open('pyladies-links.csv', 'w', encoding='utf8') as fout:
    for record in records:
        if record.img:
            continue

        fout.write(f'{record.text}: {record["href"]}\n')


