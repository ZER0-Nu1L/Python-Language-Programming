#用户登录的三次机会.py
count = 0
Tadmin = "Kate"
Tpassword = "666666"

while True:
    if count == 3:
        print("3次用户名或者密码均有误！退出程序。")
        break
    admin = input("")
    password = input("")
    if( admin == Tadmin and password == Tpassword):
        print("登录成功！")
        break
    else:
        count += 1
