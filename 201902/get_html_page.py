import requests  # ①

res = requests.get('https://pyladiestokyo.github.io/')  # ②
print(res.content)  # ③

with open('pyladies-top.html', 'wb') as fout:
    fout.write(res.content)
