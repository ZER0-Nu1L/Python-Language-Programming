#CaesarCode_Encryption.py
plaincode = input("请输入明文")
for p in plaincode:
    if ord("a") <= ord(p) <= ord("z"):         #可以这样吗？？
        print(chr( ord("a") + (ord(p) - ord("a") + 3) % 26), end = "")  #不可以简单的用加减法的原因
    else:
        print(p, end= "")
