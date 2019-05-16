#Draw-Mypython
import turtle as t
t.setup(650, 350, 200, 200)
t.pu()
t.fd(-250)
t.pendown()
t.pensize(30)#
t.pencolor("red")
t.seth(-40)


for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40, 80/2)
t.fd(40)
t.circle(16, 180)
t.fd(30)
t.done()
