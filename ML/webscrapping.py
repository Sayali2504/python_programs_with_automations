import bs4
import requests

res = requests.get("")

print(type(res))

print(res.text)

title = soup.select('title')
