#AuoTace_Draw.py
import turtle as t

def main():
    initialize()
    data = []
    dataInput(data)
    drawLine(data)

def initialize():
    t.title("自动轨迹绘制")
    t.setup(600,800,0,0)
    t.pencolor("red")

def dataInput(data):
    f = open("data.txt","r")
    for line in f:
        line = line.replace("\n", "")#
        lst = list(map(eval,line.split(",")))#
        data.append(lst)
    f.close()

def drawLine(data):
    for i in range(len(data)):
        t.pencolor(data[i][3],data[i][4],data[i][5])
        t.fd(data[i][0])
        if data[i][1] == 1:
            t.right(data[i][2])
        else:
            t.left(data[i][2])
main()
