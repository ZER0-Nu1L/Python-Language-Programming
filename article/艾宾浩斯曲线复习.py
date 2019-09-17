#艾宾浩斯曲线复习.py
import time
time = time.localtime(time.time())
year, month, day = time.tm_year, time.tm_mon, time.tm_mday
count = 1
day+=1
for du in (1, 2, 4, 7, 15):
    print(count, end=" ")
    count +=1
    if(day > du):
        print(month,day-du, sep=".")
    
