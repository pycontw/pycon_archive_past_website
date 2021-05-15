import requests
import os
from bs4 import BeautifulSoup 
from urllib.parse import unquote

Pycon_url = "https://tw.pycon.org"

def mkdir(path):
    try:
        # 1) correct the path to directory path and be a local path
        # 2) by using unquote to avoid the Garbled path
        dir = '.' + path[0:path.rfind('/') + 1]
        dir = unquote(dir)
        if not os.path.exists(os.path.dirname(dir)):
            os.makedirs(dir)
    except OSError as err:
        print(err)

def writefile(path):
    # request to the Pycon path, and fetch it to local file by using binary writing
    request = requests.get(Pycon_url + path)
    file = '.' + unquote(path)
    with open(file, 'wb') as f:
        f.write(request.content)

def script(soup):
    for script in soup.find_all("script"):
        # if the tag has the attribute 'src'
        if script.attrs.get("src"):
            mkdir(script["src"])
            writefile(script["src"])

def css(soup):
    for css in soup.find_all("link"):
        # if the link tag has the 'href' attribute and
        # if the target is css file and not using outer css site
        if css.attrs.get("href") and css["href"].find("https://") == -1 and css["href"].find("css") != -1:
            mkdir(css["href"])
            writefile(css["href"])

def img(soup):
    for img in soup.find_all("img"):
        mkdir(img["src"])
        writefile(img["src"])

def GetPage(path):
    # filter our target path
    if path[0] != '/':
        return
    print(path)
    request = requests.get(Pycon_url + path)
    soup = BeautifulSoup(request.text, "html.parser")
    script(soup)    # get scripts in this page
    css(soup)       # get css in this page
    img(soup)       # get imgs in this page

    # save the html
    # 1) for supporting 2 languages, I change the language href to the correct path
    # 2) by using unquote to avoid the Garbled path
    mkdir(path)
    with open('.' + path + 'index.html', 'w') as f:
        html = str(soup).replace("<a data-lang=\"zh-hant\" href=\"#\">", "<a data-lang=\"zh-hant\" href=\"" + path.replace("en-us", "zh-hant") + "\">")
        html = html.replace("<a data-lang=\"en-us\" href=\"#\">", "<a data-lang=\"en-us\" href=\"" + path.replace("zh-hant", "en-us") + "\">")
        f.write(unquote(html))

def main():
    # Get Pycon 2016, default to zh-hant
    request = requests.get(Pycon_url + "/2016/zh-hant/")    # Get HTML
    soup = BeautifulSoup(request.text, "html.parser")       # Using html parser
    navs = soup.select("nav a")                             # Get each <a> tag in <nav> and save in navs
    
    for nav in navs:                                        # Get each page in navs and deal with en-us at the same time
        GetPage(nav["href"])
        GetPage(nav["href"].replace("zh-hant", "en-us"))

main()
