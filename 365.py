import turtle
# 定义画圆函数
def draw_circle(x, y, r):
turtle.penup()
turtle.goto(x, y - r)
turtle.pendown()
turtle.circle(r)
# 定义画矩形函数
def draw_rect(x, y, w, h):
turtle.penup()
turtle.goto(x - w / 2, y - h / 2)
turtle.pendown()
turtle.fd(w)
turtle.right(90)
turtle.fd(h)
turtle.right(90)
turtle.fd(w)
turtle.right(90)
turtle.fd(h)
# 画身体
turtle.color('yellow')
draw_circle(0, 0, 100)
# 画眼睛
turtle.color('white')
draw_circle(-40, 120, 20)
draw_circle(40, 120, 20)
turtle.color('black')
draw_circle(-40, 130, 10)
draw_circle(40, 130, 10)
# 画嘴巴
turtle.color('red')
turtle.penup()
turtle.goto(-60, 90)
turtle.pendown()
turtle.right(90)
turtle.circle(60, 180)
# 画耳朵
turtle.color('yellow')
draw_circle(-60, 200, 20)
draw_circle(60, 200, 20)
turtle.color('black')
draw_circle(-70, 220, 10)
draw_circle(50, 220, 10)
# 画脚
turtle.color('white')
draw_rect(-70, -30, 30, 60)
draw_rect(40, -30, 30, 60)
turtle.done()
