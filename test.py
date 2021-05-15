import requests
import os
from bs4 import BeautifulSoup 
from urllib.parse import urljoin, unquote

def mkdir(path):
    try:
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(path)
        return True
    except OSError as err:
        return err

r = requests.get("https://tw.pycon.org/2016/zh-hant/") #將此頁面的HTML GET下來
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
sel = soup.select("nav a") #取HTML標中的 <nav></nav> 中的<a>標籤存入sel
for s in sel:
    if s["href"][0] == '/':
        print(s["href"], s.text) 

for s in sel:
    if s["href"][0] == '/':
        path = s["href"]
        r = requests.get("https://tw.pycon.org" + path)
        soup = BeautifulSoup(r.text,"html.parser")
        path = '.' + path
        if mkdir(path):
            # script
            url = "https://tw.pycon.org" + path[1:0]
            for script in soup.find_all("script"):
                if script.attrs.get("src"):
                    # if the tag has the attribute 'src'
                    script_url = urljoin(url, script.attrs.get("src"))
                    script_dir = './' + script_url.lstrip("https://tw.pycon.org")
                    script_dir = script_dir[0:script_dir.rfind('/') + 1]
                    mkdir(script_dir)
                    r = requests.get(script_url)
                    script_soup = BeautifulSoup(r.text,"html.parser")
                    script_js = './' + script_url.lstrip("https://tw.pycon.org")
                    f = open(script_js, 'wb')
                    f.write(r.content)
                    f.close
            # css
            for css in soup.find_all("link"):
                if css.attrs.get("href"):
                    # if the link tag has the 'href' attribute
                    css_url = urljoin(url, css.attrs.get("href"))
                    if css_url.find("https://tw.pycon.org") != -1 and css_url.find("css") != -1:
                        css_dir = './' + css_url.lstrip("https://tw.pycon.org")
                        css_dir = css_dir[0:css_dir.rfind('/') + 1]
                        if mkdir(css_dir):
                            r = requests.get(css_url)
                            css_soup = BeautifulSoup(r.text,"html.parser")
                            css_css = './' + css_url.lstrip("https://tw.pycon.org")
                            f = open(css_css, 'wb')
                            f.write(r.content)
                            f.close
            # img

            for img in soup.find_all("img"):
                img_url = urljoin(url, img["src"])
                img_dir = '.' + img["src"]
                img_dir = img_dir[0:img_dir.rfind('/') + 1]
                if mkdir(unquote(img_dir)):
                    r = requests.get(img_url)
                    img_img = '.' + unquote(img["src"])
                    f = open(img_img, 'wb')
                    f.write(r.content)
                    f.close

            # html
            r = requests.get("https://tw.pycon.org" + path)
            f = open(path + 'index.html', 'w')
            html = str(soup).replace("<a data-lang=\"zh-hant\" href=\"#\">", "<a data-lang=\"zh-hant\" href=\"" + path[1:] + "\">")
            html = html.replace("<a data-lang=\"en-us\" href=\"#\">", "<a data-lang=\"en-us\" href=\"" + path.replace("zh-hant", "en-us")[1:] + "\">")
            f.write(unquote(html))
            f.close()


r = requests.get("https://tw.pycon.org/2016/en-us/") #將此頁面的HTML GET下來
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
sel = soup.select("nav a") #取HTML標中的 <nav></nav> 中的<a>標籤存入sel
for s in sel:
    if s["href"][0] == '/':
        print(s["href"], s.text) 

for s in sel:
    if s["href"][0] == '/':
        path = s["href"]
        r = requests.get("https://tw.pycon.org" + path)
        soup = BeautifulSoup(r.text,"html.parser")
        path = '.' + path
        if mkdir(path):
            # script
            url = "https://tw.pycon.org" + path[1:0]
            for script in soup.find_all("script"):
                if script.attrs.get("src"):
                    # if the tag has the attribute 'src'
                    script_url = urljoin(url, script.attrs.get("src"))
                    script_dir = './' + script_url.lstrip("https://tw.pycon.org")
                    script_dir = script_dir[0:script_dir.rfind('/') + 1]
                    mkdir(script_dir)
                    r = requests.get(script_url)
                    script_soup = BeautifulSoup(r.text,"html.parser")
                    script_js = './' + script_url.lstrip("https://tw.pycon.org")
                    f = open(script_js, 'wb')
                    f.write(r.content)
                    f.close
            # css
            for css in soup.find_all("link"):
                if css.attrs.get("href"):
                    # if the link tag has the 'href' attribute
                    css_url = urljoin(url, css.attrs.get("href"))
                    if css_url.find("https://tw.pycon.org") != -1 and css_url.find("css") != -1:
                        css_dir = './' + css_url.lstrip("https://tw.pycon.org")
                        css_dir = css_dir[0:css_dir.rfind('/') + 1]
                        if mkdir(css_dir):
                            r = requests.get(css_url)
                            css_soup = BeautifulSoup(r.text,"html.parser")
                            css_css = './' + css_url.lstrip("https://tw.pycon.org")
                            f = open(css_css, 'wb')
                            f.write(r.content)
                            f.close
            # img

            for img in soup.find_all("img"):
                img_url = urljoin(url, img["src"])
                img_dir = '.' + img["src"]
                img_dir = img_dir[0:img_dir.rfind('/') + 1]
                if mkdir(unquote(img_dir)):
                    r = requests.get(img_url)
                    img_img = '.' + unquote(img["src"])
                    f = open(img_img, 'wb')
                    f.write(r.content)
                    f.close

            # html
            r = requests.get("https://tw.pycon.org" + path)
            f = open(path + 'index.html', 'w')
            html = str(soup).replace("<a data-lang=\"zh-hant\" href=\"#\">", "<a data-lang=\"zh-hant\" href=\"" + path.replace("en-us", "zh-hant")[1:] + "\">")
            html = html.replace("<a data-lang=\"en-us\" href=\"#\">", "<a data-lang=\"en-us\" href=\"" + path[1:] + "\">")
            f.write(unquote(html))
            f.close()