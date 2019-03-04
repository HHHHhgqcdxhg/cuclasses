import json
import requests
from bs4 import BeautifulSoup
bs = BeautifulSoup
from concurrent import futures
import os
import functools

cookiesRaw = """[
{
    "domain": ".exhentai.org",
    "hostOnly": false,
    "httpOnly": false,
    "name": "igneous",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "df9724040",
    "id": 1
},
{
    "domain": ".exhentai.org",
    "hostOnly": false,
    "httpOnly": false,
    "name": "ipb_member_id",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "4483572",
    "id": 2
},
{
    "domain": ".exhentai.org",
    "hostOnly": false,
    "httpOnly": false,
    "name": "ipb_pass_hash",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "b1d7d5acd649a01a1643124c8a0918a8",
    "id": 3
}
]"""
cookies = json.loads(cookiesRaw)
cookies = {cookie["name"]:cookie["value"] for cookie in cookies}

headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

def getPages(indexUrl):
    res = requests.get(indexUrl,cookies=cookies,headers=headers)
    html = res.text
    soup = BeautifulSoup(html,"lxml")
    return [page["href"] for page in  soup.select("div#gdt a")]

def getPageSetuURL(pageURL):
    res = requests.get(pageURL,headers=headers,cookies=cookies)
    html = res.text
    soup = bs(html,"lxml")
    img = soup.find("img",id="img")
    return img["src"]

def getPageSetu(saveDire,pageURL):
    imgURL = getPageSetuURL(pageURL)
    res = requests.get(imgURL,headers=headers,cookies=cookies)
    fileName = os.path.split(imgURL)[-1]
    filePath = os.path.join(saveDire,fileName)
    print(filePath)
    with open(filePath,"wb") as f:
        f.write(res.content)

def getSetu(indexURL:"exhentai本子主页",saveDire,maxWorks=20):
    pages = getPages(indexURL)
    getPageSetu_ = functools.partial(getPageSetu,saveDire)
    with futures.ThreadPoolExecutor(maxWorks) as exe:
        exe.map(getPageSetu_,pages)


if __name__ == '__main__':
    savePath = r"E:\ACG\comic\r\NL\泡姬\11"
    indexURL = "https://exhentai.org/g/1260338/952e2eb3fa/"

    getSetu(indexURL,savePath,10)
