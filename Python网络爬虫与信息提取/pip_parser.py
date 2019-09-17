#pip_parser.py
import os
lib = {"lxml","html5lib"}
try:
    for item in lib:
        os.system("pip install "+item)
    print("下载成功")
except:
    print("出现异常")
