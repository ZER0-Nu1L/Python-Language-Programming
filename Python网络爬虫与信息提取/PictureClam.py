#PictureClam.py
import requests
import os

url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1550633671379&di=905d51e34d1e92dacb826bbb2ad3855c&imgtype=0&src=http%3A%2F%2Fphotocdn.sohu.com%2F20150909%2Fmp31139342_1441765361306_3.gif"
root = "D://pics//"
path = root + url.split("/")[-1]#保留原名的方法
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        #r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已经存在")
except:
    print("爬取失败")
    print(r.status_code)

'''
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            with open(path) as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        except:
            print("产生异常")
    else:
        print("文件已经存在")
except:
    print("爬取失败")
'''