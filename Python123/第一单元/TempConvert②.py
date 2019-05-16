#温度转化②.py
TemptStr = input("")
if TemptStr[0] in ['F', 'f']:
    C = (eval(TemptStr[1: ]) - 32)/1.8
    print("C{:.2f}".format(C))
elif TemptStr[0] in ['C', 'c']:
    F = eval(TemptStr[1: ]) * 1.8 + 32
    print("F{:.2f}".format(F))
