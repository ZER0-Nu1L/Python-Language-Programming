#P74 DayDayUp3.py

dayup, dayfactor  = 1.0, 0.01
for i in range(365):
    if i % 7 in [0, 6]:
        dayup *= (1 - dayfactor)
    else:
        dayup *= (1 + dayfactor)
print("向上5天向下2天的结果：{:.2f}".format(dayup))
