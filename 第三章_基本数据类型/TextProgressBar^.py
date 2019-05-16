#TextProgressBar^.py
import time
scale = 30
print("开始执行".center(40, "*"))
for i in range(scale+1):
    a = "-" * i
    b = "." * (scale - i)
    c = i / scale
    time.sleep(0.10)
    print("\r{:>5.0%}[{}->{}]".format(c, a, b), end = "")
print("执行结束".center(40, "*"))
