#jingdong.py
import requests


url = "https://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    #print(r.status_code)
    r.raise_for_status()
    r.encoding = r.aparent_encoding
    print(r.txt[:1000])
except:
    print("产生异常")
