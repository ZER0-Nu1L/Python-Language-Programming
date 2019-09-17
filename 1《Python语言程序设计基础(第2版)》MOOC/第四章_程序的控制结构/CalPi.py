#CalPi.py
'''使用蒙特卡落方法计算圆周率
random；随机次数；
'''
from random import random
from math import sqrt
import time

DART = 100000000
count = 0
start = time.perf_counter()
for i in range(DART):
    x, y = random(), random()
    if( sqrt(x**2 + y**2) < 1):
        count += 1
print("Pi值是：{}".format(count/DART*4))
print("运行时间是：{}s".format(time.perf_counter() - start))
