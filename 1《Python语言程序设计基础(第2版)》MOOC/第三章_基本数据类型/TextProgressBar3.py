#TextProgressBar3.py
import time
scale = 50
print("开始执行".center(scale//2, "*"))
start = time.perf_counter()
for i in range(scale+1):
    a = "-" * i
    b = "." * (scale - i)
    c = i / scale
    duration = time.perf_counter() - start
    print("\r{:>4.0%}[{}->{}]{:.2f}s".format(c, a, b, duration), end = "")
    time.sleep(0.10)
print("\n"+"执行结束".center(scale//2, "*"))
