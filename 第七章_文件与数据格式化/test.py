#test.py
f1 = open("test.txt","r")
txt = f1.read().split(",")
f1.close()
for item in txt:
    print(item)

f2 = open("test0.txt","x")
f2.write(" ".join(txt))
f2.close()