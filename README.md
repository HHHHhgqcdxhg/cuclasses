# Cuclasses

## 介绍
Cuclasses是我正在写的python库,内容是集合了一些常用的类和方法  
## 项目地址
pypi(少有更新):[https://pypi.org/project/cuclasses/](https://pypi.org/project/cuclasses/)
github:[https://github.com/HHHHhgqcdxhg/cuclasses](https://github.com/HHHHhgqcdxhg/cuclasses)
## 模块
#### cuclasses.DottableDict
顾名思义,能用 "." 访问的dict.因为喜欢js访问对象属性的方式,可以用下标,也可以用点.  
#### cuclasses.singleton
装饰器.  
被装饰的类为单例模式
#### cuclasses.CallableDict
可以调用的dict,调用时返回自身.
#### cuclasses.StrKeyDict
在查询时把非字符串键转换为字符串的dict
#### cuclasses.headerCopy2Dict
因为在复制chrome开发者工具network里请求的header时很不方便,就弄了这个...把chrome里的headers复制进去,会转换成字典  

```python
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
#>>> {'Accept': 'application/json, text/plain, */*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Connection': 'keep-alive', 'Host': 'message.bilibili.com', 'Origin': 'https://www.bilibili.com', 'Referer': 'https://www.bilibili.com/video/av9912938/?p=11', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
```

#### cuclasses.timePrint
上下文管理器.  
带时间戳的print.随时可指定时间格式  

```python
with timePrint() as print:
    print(0)
    # >>> [2019-02-10 16:23:35] 0

    print(1, strf="[%Y-%m-%d %H:%M:%S]1")
    # >>> [2019-02-10 16:23:35]1 1

with timePrint("[%Y-%m-%d %H:%M:%S]2") as print:
    print(2)
    # >>> [2019-02-10 16:23:35]2 2

    print(3, strf="[%Y-%m-%d %H:%M:%S]3")
    # >>> [2019-02-10 16:23:35]3 3

print(4)
# >>> 4
```

#### cuclasses.timeCount
装饰器.接受两个参数.
被装饰的函数将在执行后打印执行时间  

```
:param enable: 设为False则不计时,直接执行函数
:param method: 可选择的计时所用的获取时间的函数.默认time.perf_counter,或者也可以选填time.time,python3.7可以按需选用time.perf_counter_ns
```
  

```python
@timeCount()
def bar():
    print({"a": "c"})

bar()
#>>> {'a': 'c'}
#>>> func bar          excuted in : 6.044444444444444e-05
```

#### cuclasses.Downloader
下载器.  

```
:param directory:下载到的目录
:param urls:需要下载的资源目录
:param threads:并行下载的线程数
:param headers:请求头,默认为{"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
```

  
```python
with open("xx.json","r") as f:
    data = json.load(f)
d = Downloader(directory=r"E:\ACG\comic\general\どうして私が美術科に",urls=data)
d.downloadAll()
```  
  
