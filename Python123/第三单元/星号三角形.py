#星号三角形.py
n = eval(input(""))
for i in range( (n+1)//2 ):
    str = "*" * (2 * i + 1)
    print(str.center(n))

"""
n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))
"""
