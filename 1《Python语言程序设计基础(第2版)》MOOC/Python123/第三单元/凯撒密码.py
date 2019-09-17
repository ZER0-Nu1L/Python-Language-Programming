#凯撒密码.py
plaincode  = input("")
for c in plaincode:
    if ord("a") <= ord(c) <= ord("z"):
        print(chr( (ord(c) - ord("a") + 3) % 26 + ord("a")), end = "")
    elif ord("A") <= ord(c) <= ord("Z"):
        print(chr( (ord(c) - ord("A") + 3) % 26 + ord("A")), end = "")
    else:
        print(c, end = "")
