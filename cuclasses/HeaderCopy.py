def headerCopy2Dict(headerStr: str):
    d = {kv.split(":")[0].rstrip(): ":".join(kv.split(":")[1:]).lstrip() for kv in headerStr.split("\n")}
    if "Cookie" in d:
        # d["Cookie"] = cookiesCopy2Dict(d["Cookie"])
        del d["Cookie"]
    return d


cookiesCopy2Dict = lambda cookieStr: {kv.split("=")[0].lstrip(): kv.split("=")[1] for kv in cookieStr.split(";")}
if __name__ == '__main__':
    headerStr = """Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Cookie: l=v; buvid3=08DBF55E-086D-4BE2-9FCB-4B60BFA5F05A140254infoc
Host: message.bilibili.com
Origin: https://www.bilibili.com
Referer: https://www.bilibili.com/video/av9912938/?p=11
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"""
    a = headerCopy2Dict(headerStr)
    print(a)
    print(a["Cookie"])
