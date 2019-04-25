#画中国象棋棋盘
import turtle
import math
turtle.speed(10)#绘图速度
a = 30           #每个格子的宽度

#绘制底板并上色
turtle.up()
turtle.goto( 0, 0)
turtle.down()
turtle.fillcolor("Khaki")
turtle.begin_fill()
turtle.fd( a * 8 + 20)
turtle.left(90)
turtle.fd( a * 9 + 20)
turtle.left(90)
turtle.fd( a * 8 + 20)
turtle.left(90)
turtle.fd( a * 9 + 20)
turtle.left(90)
turtle.end_fill()

#画笔回位
turtle.up()
turtle.goto(0,0)
turtle.down()

#画横线
for i in range(10):
    turtle.fd( a * 8 )
    turtle.up()
    turtle.bk( a * 8)
    turtle.left( 90 )
    turtle.fd( a )
    turtle.right( 90 )
    turtle.down()
turtle.up()
turtle.goto( 0, 0)
turtle.down()

#画竖线
turtle.left(90)
for i in range(9):
    if i == 0 or i == 8:
        turtle.fd( a * 9 )
        turtle.up()
        turtle.bk( a * 9 )
        turtle.right(90)
        turtle.fd(a)
        turtle.left(90)
        turtle.down()
    else:
        turtle.fd( a * 4 )
        turtle.up()
        turtle.fd(a)
        turtle.down()
        turtle.fd( a * 4)
        turtle.up()
        turtle.bk( a * 9)
        turtle.right(90)
        turtle.fd(a)
        turtle.left(90)
        turtle.down()

# 画米字格
turtle.up()
turtle.goto( a * 4, a)
turtle.down()
turtle.right(45)
for i in range(4):
    turtle.fd(math.sqrt( a * a * 2))
    turtle.bk(math.sqrt( a * a * 2))
    turtle.right(90)
turtle.up()
turtle.goto(a*4,a*8)
turtle.down()
for i in range(4):
    turtle.fd(math.sqrt( a * a * 2))
    turtle.bk(math.sqrt( a * a * 2))
    turtle.right(90)

turtle.done()