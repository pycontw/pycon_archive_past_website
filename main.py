from bs4.element import PY3K
import requests
import json
import os
import re
from bs4 import BeautifulSoup 
from urllib.parse import unquote

Pycon_year = "2019"
Pycon_url = "https://tw.pycon.org"
Written_url = []

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
    Written_url.append(path)
    request = requests.get(Pycon_url + path)
    file = '.' + unquote(path)
    try:
        with open(file, 'wb') as f:
            f.write(request.content)
    except OSError as err:
        print(err)

def getcssimg(path):
    # get all url like /year/... target, and try to save them all.
    file = '.' + path
    with open(file, 'rb') as f:
        content = str(f.read())
        all_url = re.findall('/' + Pycon_year + '[^\s]*', content)
        for url in all_url:
            url = url.replace('\\n', '')
            url = url[0:url.rfind('\\')]
            url = url[0:url.rfind('?')]
            if url not in Written_url:
                mkdir(url)
                writefile(url)
            

def script(soup):
    for script in soup.find_all("script"):
        # get all url like /year/... target, and try to save them all.
        all_url = re.findall('/' + Pycon_year + '[^\s]*', str(script))
        for url in all_url:
            url = url[0:max(url.rfind('\''), url.rfind('\"'))]
            if url not in Written_url:
                mkdir(url)
                writefile(url)

def css(soup):
    for css in soup.find_all("link"):
        # if the link tag has the 'href' attribute and
        # if the target is css file and not using outer css site
        if css.attrs.get("href") and css["href"].find("https://") == -1 and css["href"].find("css") != -1 and css["href"] not in Written_url:
            mkdir(css["href"])
            writefile(css["href"])
            getcssimg(css["href"])

def img(soup):
    for img in soup.find_all("img"):
        # if img has attr src
        if img.attrs.get("src"):
            mkdir(img["src"])
            writefile(img["src"])
    # get imgs in json, especially for pycon /2017/zh-hant/events/keynotes/
    for script in soup.find_all("script", type="application/json"):
        json_object = json.loads(script.contents[0])
        if "keynote" in json_object:
            for person in json_object["keynote"]:
                mkdir(person['photo'])
                writefile(person['photo'])

def GetPage(path):
    # filter our target path
    if path[0] != '/':
        return
    print(path)
    request = requests.get(Pycon_url + path)
    soup = BeautifulSoup(request.content, "html.parser")
    script(soup)    # get scripts in this page
    css(soup)       # get css in this page
    img(soup)       # get imgs in this page
    # save the html
    # 1) for supporting 2 languages, each pycon year will deal separately.
    # 2) by using unquote to avoid the Garbled path
    mkdir(path)
    with open('.' + path + 'index.html', 'w') as f:
        for input in soup.find_all("input", {'name':'csrfmiddlewaretoken'}): 
            input.decompose()
        if Pycon_year == '2017':
            if path[6:8] == 'zh':
                elements = soup.find_all("a", {'data-lang':'en-us'})
                for elm in elements:
                    elm.replace_with("en-us_target")
            if path[6:8] == 'en':
                elements = soup.find_all("a", {'data-lang':'zh-hant'})
                for elm in elements:
                    elm.replace_with("zh-hant_target")
        html = str(soup)
        html = html.replace("action=\"/" + Pycon_year + "/set-language/\"", "")
        if Pycon_year == '2016':
            html = html.replace("<a data-lang=\"zh-hant\" href=\"#\">", "<a data-lang=\"zh-hant\" href=\"" + path.replace("en-us", "zh-hant") + "\">")
            html = html.replace("<a data-lang=\"en-us\" href=\"#\">", "<a data-lang=\"en-us\" href=\"" + path.replace("zh-hant", "en-us") + "\">")
        if Pycon_year == '2017':
            if path[6:8] == 'zh':
                html = html.replace("en-us_target", "<div data-lang=\"en-us\" style=\"margin-left: 40px; line-height: 60px;\"> <a href='" + path.replace("zh-hant", "en-us") + "' style=\"font-size: 16px;\">English (US)</a></div>", 1)
                html = html.replace("en-us_target", "<div data-lang=\"en-us\" style=\"margin-left: 20px;\"> <a href='" + path.replace("zh-hant", "en-us") + "'>English (US)</a></div>", 1)
            if path[6:8] == 'en':
                html = html.replace("zh-hant_target", "<div data-lang=\"zh-hant\" style=\"margin-left: 40px; line-height: 60px;\"> <a href='" + path.replace("en-us", "zh-hant") + "' style=\"font-size: 16px;\">繁體中文</a></div>", 1)
                html = html.replace("zh-hant_target", "<div data-lang=\"zh-hant\" style=\"margin-left: 20px;\"> <a href='" + path.replace("en-us", "zh-hant") + "'>繁體中文</a></div>", 1)
        if Pycon_year == '2018':
            if path[6:8] == 'zh':
                html = html.replace("EN", "<a href='" + path.replace("zh-hant", "en-us") + "' class=\"myclass\">EN</a>", 1)
            if path[6:8] == 'en':
                html = html.replace("ZH", "<a href='" + path.replace("en-us", "zh-hant") + "' class=\"myclass\">ZH</a>", 1)
            html += "<style>.myclass{text-decoration: none;color: rgba(255, 255, 255, 0.35);}.myclass:hover{text-decoration: none;color: rgba(255, 255, 255, 0.7);}</style>"
        if Pycon_year == '2019':
            if path[6:8] == 'zh':
                html = html.replace("EN", "<a href='" + path.replace("zh-hant", "en-us") + "' class=\"myclass\">EN</a>", 1)
            if path[6:8] == 'en':
                html = html.replace("ZH", "<a href='" + path.replace("en-us", "zh-hant") + "' class=\"myclass\">ZH</a>", 1)
            html += "<style>.myclass{text-decoration: none;color: #616e86;}.myclass:hover{text-decoration: none;color: #4a5363;}</style>"
        f.write(unquote(html))

def main():
    # Get Pycon 2016, default to zh-hant
    request = requests.get(Pycon_url + "/" + Pycon_year + "/zh-hant/")    # Get HTML
    soup = BeautifulSoup(request.text, "html.parser")       # Using html parser
    navs = soup.select("nav a")                             # Get each <a> tag in <nav> and save in navs
    navs = set([nav["href"] for nav in navs])               # Get each href in navs, and make it unique
    
    for nav in navs:                                        # Get each page in navs and deal with en-us at the same time
        GetPage(nav)
        GetPage(nav.replace("zh-hant", "en-us"))

main()
