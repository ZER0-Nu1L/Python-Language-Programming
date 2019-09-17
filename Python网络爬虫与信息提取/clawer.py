#clawer.py
import requests
import time

start = time.perf_counter()
for i in range(100):
    print("第{}次爬虫百度".format(i+1))
    try:
        r = requests.get("http://www.baidu.com")
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print("爬虫成功")
    except:
        print("产生异常")
sumtime = time.perf_counter() - start
print("总共用时{:.2f}s".format(sumtime))
