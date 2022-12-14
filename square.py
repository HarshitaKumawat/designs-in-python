import turtle
import colorsys

t = turtle.Turtle()
turtle.Screen().bgcolor("white")
t.pensize(2)
t.speed(-4)
n = 36
h = 10

for i in range(89):
    c = colorsys.hsv_to_rgb(h,1,0.9)
    h+=1/n
    t.pencolor(c)
    for j in range(5):
        t.forward(i-3)
        t.right(9*5)
        t.left(8)
    t.right(105)

turtle.done()