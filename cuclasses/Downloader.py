import requests as req
import json
import os
from concurrent import futures

class Downloader:
    def __init__(self, directory, urls=[], threads=20, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}):
        """
        :param directory:下载到的目录
        :param urls:需要下载的资源目录
        :param threads:并行下载的线程数
        :param headers:请求头,默认为{"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
        """
        self.directory = directory
        self.urls = urls
        self.headers = headers
        self.threads = threads
        self.count = self.urls.__len__()

    def downloadOne(self, url, directory=None):
        if directory is None:
            directory = self.directory
        fileName = url.split("/")[-1].split("?")[0]
        filePath = os.path.join(directory, fileName)
        with open(filePath, "wb") as f:
            res = req.get(url, headers=self.headers)
            f.write(res.content)
    def downloadAll(self):
        handdled = 0
        with futures.ProcessPoolExecutor(self.threads) as exe:
            all_task = [exe.submit(self.downloadOne, (file)) for file in self.urls]
            for future in futures.as_completed(all_task):
                handdled += 1
                print(f"{handdled}/{self.count} handdled")

if __name__ == '__main__':
    with open("xx.json","r") as f:
        data = json.load(f)
        print(data)
    headers = {
        "referer": "https://twitter.com/py_py_ai/media",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
    }
    d = Downloader(directory=r"E:\ACG\comic\general\どうして私が美術科に",urls=data,headers=headers)
    d.downloadAll()
