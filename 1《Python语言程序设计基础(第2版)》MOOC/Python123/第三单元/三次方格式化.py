#三次方格式化.py
a = eval(input(""))     #eval()
a **= 3
if a == int(a):
    print("{:-^20d}".format(a))
else:
    print("{:-^20f}".format(a))# fomat & center
