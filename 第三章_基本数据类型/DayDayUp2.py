#P74 DayDayUp2.py
dayfactor = eval(input("请输入每天学与不学能力值的偏移量：") )
#int(input("请输入每天学与不学能力值的偏移量："))不能保证输入的是整数型
dayup = pow(1+ dayfactor, 365)
daydown = pow(1-dayfactor, 365)
print("向上：{:.2f}\n向下：{:.2f}".format(dayup, daydown))
