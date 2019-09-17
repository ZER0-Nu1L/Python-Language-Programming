#baidu-keyword.py
import requests
keyword = "Python"
kv = {'wd':keyword}
try:
    r = requests.get("https://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
except:
    print("产生异常")
