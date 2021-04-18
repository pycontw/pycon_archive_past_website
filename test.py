import requests
from bs4 import BeautifulSoup 

r = requests.get("https://tw.pycon.org/2016/zh-hant/") #將此頁面的HTML GET下來
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
sel = soup.select("nav a") #取HTML標中的 <nav></nav> 中的<a>標籤存入sel
for s in sel:
    if s["href"][0] == '/':
        print(s["href"], s.text) 

for s in sel:
    if s["href"][0] == '/':
        r = requests.get("https://tw.pycon.org" + s["href"])
        soup = BeautifulSoup(r.text,"html.parser")
        print(soup)
        print("=======================")
