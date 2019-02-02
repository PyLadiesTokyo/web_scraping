import requests  # ①

res = requests.get('https://www.pyladies.com/locations/')  # ②
print(res.content)  # ③

with open('pyladies-locations.html', 'wb') as fout:
    fout.write(res.content)
