#CaesarCode_Decode.py
plaincode = input("请输入一段秘文")
for p in plaincode:
    if ord("a") <= ord(p) <= ord("z"):
        print( chr( (ord(p) - ord("a") - 3) % 26 + ord("a")), end = "" )
    else:
        print(p, end = '')
