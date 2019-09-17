#RoseDraw.py
import turtle as t
import time
# 定义一个曲线绘制函数

def DegreeCurve(n, r, d=1):
    for i in range(n):
        t.left(d)
        t.circle(r, abs(d))
# 初始位置设定
s = 0.2 # size
t.setup(450*5*s, 800*4*s, 300, 10)
t.pencolor("black")
t.fillcolor("red")
t.speed(100)
t.penup()
t.goto(0, 900*s)
t.pendown()

# 绘制花朵形状
t.speed("fastest")
t.begin_fill()
t.circle(200*s,30)
DegreeCurve(60, 50*s)
t.circle(200*s,30)
DegreeCurve(4, 100*s)
t.circle(200*s,50)
DegreeCurve(50, 50*s)
t.circle(350*s,65)
DegreeCurve(40, 70*s)
t.circle(150*s,50)
DegreeCurve(20, 50*s, -1)
t.circle(400*s,60)
DegreeCurve(18, 50*s)
t.fd(250*s)
t.right(150)
t.circle(-500*s,12)
t.left(140)
t.circle(550*s,110)
t.left(27)
t.circle(650*s,100)
t.left(130)
t.circle(-300*s,20)
t.right(123)
t.circle(220*s,57)
t.end_fill()
# 绘制花枝形状
t.speed("fastest")
t.left(120)
t.fd(280*s)
t.left(115)
t.circle(300*s,33)
t.left(180)
t.circle(-300*s,33)
DegreeCurve(70, 225*s, -1)
t.circle(350*s,104)
t.left(90)
t.circle(200*s,105)
t.circle(-500*s,63)
t.penup()
t.goto(170*s,-30*s)
t.pendown()
t.left(160)
DegreeCurve(20, 2500*s)
DegreeCurve(220, 250*s, -1)
# 绘制一个绿色叶子
t.speed("slow")
t.fillcolor('green')
t.penup()
t.goto(670*s,-180*s)
t.pendown()
t.right(140)
t.begin_fill()
t.circle(300*s,120)
t.left(60)
t.circle(300*s,120)
t.end_fill()
t.penup()
t.goto(180*s,-550*s)
t.pendown()
t.right(85)
t.circle(600*s,40)
# 绘制另一个绿色叶子
t.speed("slow")
t.penup()
t.goto(-150*s,-1000*s)
t.pendown()
t.begin_fill()
t.rt(120)
t.circle(300*s,115)
t.left(75)
t.circle(300*s,100)
t.end_fill()
t.penup()
t.goto(430*s,-1070*s)
t.pendown()
t.right(30)
t.circle(-600*s,35)
#==================================打字===========================================
t.speed("slowest")
t.pu()
t.goto(-200,250)
t.seth(-90)
for c in "我不懂浪漫":
    t.pd()
    t.write(c, font = ("Arral", 14, "normal"))
    t.pu();t.fd(20)
time.sleep(1)
t.fd(25)
for c in "但我懂你":
    t.pd()
    t.write(c, font = ("Arral", 14, "normal"))
    t.pu();t.fd(20)
time.sleep(1)

t.fd(110);t.left(90)
for c in "杨莹莹":
    t.pd()
    t.write(c, font = ("Arral", 18, "normal"))
    t.pu();t.fd(25)
time.sleep(1)

t.goto(-200, -100)

t.pencolor("red")
for c in "Ｉ Lᵒᵛᵉᵧₒᵤ❤":#๑′ᴗ‵๑ 
    t.pd()
    t.write(c, font = ("Arral", 18, "normal"))
    t.pu();t.fd(12)
t.goto(-200, -140)

for c in "by ":#๑′ᴗ‵๑ 
    t.pd()
    t.write(c, font = ("Arral", 18, "normal"))
    t.pu();t.fd(10)

t.pencolor("black")
for c in "吴昌博":#๑′ᴗ‵๑ 
    t.pd()
    t.write(c, font = ("Arral", 18, "normal"))
    t.pu();t.fd(25)
t.goto(-200, -175)

#==================================日期==================================
def DrawGap():
    t.pu()
    t.fd(1)
def DrawLine(draw):
    DrawGap()
    t.pd() if draw else t.pu()
    t.fd(8)
    DrawGap()
    t.right(90)
def DrawDigit(number):
    DrawLine(True) if number in [2,3,4,5,6,8,9] else DrawLine(False)
    DrawLine(True) if number in [0,1,3,4,5,6,7,8,9] else DrawLine(False)
    DrawLine(True) if number in [0,2,3,5,6,8,9] else DrawLine(False)
    DrawLine(True) if number in [0,2,6,8] else DrawLine(False)
    t.left(90)
    DrawLine(True) if number in [0,4,5,6,8,9] else DrawLine(False)
    DrawLine(True) if number in [0,2,3,5,6,7,8,9] else DrawLine(False)
    DrawLine(True) if number in [0,1,2,3,4,7,8,9] else DrawLine(False)
    t.left(180)
    t.pu()
    t.fd(4)
def DrawDate(date):
    t.pencolor("red")
    for i in date:
        if i == '-':
            t.write('年', font = ("Arral", 10, "normal"))
            t.pencolor("green")
            t.fd(14)
        elif i == '=':
            t.write('月', font = ("Arral", 10, "normal"))
            t.pencolor("blue")
            t.fd(6)
        elif i == '+':
            t.write('日', font = ("Arral", 10, "normal"))
        else:
            DrawDigit(eval(i))
t.speed("fastest")
t.goto(-200, -260)
DrawDate("2019-02=14+")
t.hideturtle()
t.done()
