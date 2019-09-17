#clawer.py
import requests
try:
    r = requests.get("https://item.jd.com/2967929.html")
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print("爬虫成功")
    print(r.text[:1000])
except:
    print("产生异常")
