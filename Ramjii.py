import turtle
pen = turtle.Turtle()
pen.hideturtle()

pen.forward(120)
pen.left(90)
pen.forward(50)
pen.left(90)
pen.forward(120)
pen.left(90)
pen.forward(50)

pen.penup()
pen.goto(7, 8)
pen.write('SHREE RAM', font = ('Courier', 12, 'normal'))
pen.pendown()

def button_click(x, y):
    if (x > 0) and (x < 81) and (y > 0) and (y < 30) :
        print('JAI SHREE RAM JII')
        pen.screen.bgpic('Shree_ram.gif')
        pen.screen.bgcolor('black')
        pen.speed(5)
        pen.up()
        pen.lt(270)
        pen.pencolor('white')
        pen.fd(950)
        pen.down()
        pen.pensize(5)
        pen.rt(90)
        pen.fd(480)
        pen.rt(90)
        pen.fd(1875)
        pen.rt(90)
        pen.fd(970)
        pen.rt(90)
        pen.fd(1875)
        pen.rt(90)
        pen.fd(550)
        pen.rt(90)
        pen.up()
        pen.fd(100)
        pen.lt(90)
        pen.fd(200)
        pen.down()
        pen.color('red')
        pen.rt(180)
        pen.circle(40,180)
        pen.rt(90)
        pen.fd(50)
        pen.lt(90)
        pen.fd(50)
        pen.lt(90)
        pen.fd(60)
        pen.bk(120)
        pen.fd(60)
        pen.lt(90)
        pen.fd(110)
        pen.bk(110)
        pen.lt(90)
        pen.fd(60)
        pen.lt(180)
        pen.up()
        pen.circle(25,180)
        pen.down()
        pen.circle(25,180)
        pen.up()
        pen.circle(25,180)
        pen.down()
        pen.rt(90)
        pen.circle(40,115)
        pen.setheading(0)
        pen.lt(90)
        pen.fd(85)
        pen.lt(90)
        pen.fd(30)
        pen.bk(60)
        pen.fd(30)
        pen.lt(90)
        pen.fd(109)
        pen.up()
        pen.fd(350)
        pen.down()
        pen.setheading(260)
        pen.rt(25)
        pen.fd(110)
        pen.bk(110)
        pen.rt(90)
        pen.circle(31, 175)
        pen.setheading(345)
        pen.fd(55)
        pen.setheading(240)
        pen.fd(60)
        pen.bk(60)
        pen.setheading(90)
        pen.fd(84)
        pen.lt(90)
        pen.fd(40)
        pen.bk(40)
        pen.setheading(270)
        pen.fd(140)
        pen.bk(140)
        pen.setheading(0)
        pen.fd(50)
        pen.setheading(270)
        pen.rt(180)
        pen.circle(26, 180)
        pen.up()
        pen.circle(26, 180)
        pen.down()
        pen.setheading(270)
        pen.fd(135)
        pen.up()
        pen.home()
        pen.setheading(0)
        pen.fd(500)
        pen.lt(90)
        pen.fd(200)
        pen.down()
        pen.setheading(0)
        pen.fd(300)
        pen.bk(250)
        pen.up()
        pen.setheading(270)
        pen.fd(89)
        pen.down()
        pen.setheading(0)
        pen.circle(45, 200)
        pen.up()
        pen.circle(45, 200)
        pen.down()
        pen.setheading(0)
        pen.rt(60)
        pen.fd(110)
        pen.up()
        pen.setheading(0)
        pen.fd(35)
        pen.lt(90)
        pen.down()
        pen.fd(169)
        pen.up()
        pen.rt(90)
        pen.fd(70)
        pen.rt(90)
        pen.down()
        pen.fd(100)
        pen.setheading(180)
        pen.rt(45)
        pen.fd(40)
        pen.setheading(0)
        pen.fd(80)
        pen.lt(90)
        pen.fd(76)
        pen.bk(76)
        pen.bk(100)
turtle.onscreenclick(button_click, 1)
turtle.listen()
turtle.done()