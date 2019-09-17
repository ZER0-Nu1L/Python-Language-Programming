#连续爬虫.py
import requests
import time

def main():
    start = time.perf_counter()
    for i in range(100):
        print("第{:2d}次爬虫百度".format(i+1), end = "")
        print(getHTTP())
    sumtime = time.perf_counter() - start
    print("总共用时{:.2f}s".format(sumtime))

def getHTTP():
    try:
        r = request.get("https://www.baidu.com")
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return "爬虫成功"
    except:
        return "产生异常"
main()
