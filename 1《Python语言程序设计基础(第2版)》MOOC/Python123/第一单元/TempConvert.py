#温度转化.py
TemptStr = input("")
if TemptStr[-1] in ['F', 'f']                   #in 的正反
    C = (eval(TemptStr[0:-1]) - 32)/1.8
    print("{:.2f}C".format(C))
elif TemptStr[-1] in ['C', 'c']:
    F = eval(TemptStr[0:-1]) * 1.8 + 32
    print("{:.2f}F".format(F))
else:
    print("输入格式错误")
