import requests

res = requests.get('https://tokyo.pyladies.com')
print(res.content)

with open('pyladies-top.html', 'wb') as fout:
    fout.write(res.content)
