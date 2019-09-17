#三位水仙花数.py
flag = 1
for n in range(100, 1000):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    if( a**3 + b**3 + c**3 == n):
        if(flag == 1):
            print(n, end = "")
            flag = 0
        else:
            print(",{}".format(n), end = "")
