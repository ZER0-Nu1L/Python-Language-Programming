#TextProgressBar.py
import time
scale = 10
print("开始执行".center(20, "*"))
for i in range(scale + 1):
    a = "-" * i
    b = "." * (scale - i)
    c = i / scale
    print("{:>5.0%}:[{}->{}]".format(c, a, b))
    time.sleep(0.1)
print("开始执行".center(10, "*"))
