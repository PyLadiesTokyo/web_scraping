import requests  # ①

res = requests.get('https://tokyo.pyladies.com/')  # ②
print(res.content)

with open('pyladies-top.html', 'wb') as fout:
    fout.write(res.content)