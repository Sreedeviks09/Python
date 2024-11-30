from turtle import *
speed(0)
bgcolor('black')
color('yellow')
for i in range(160):
    rt(i)
    circle(160,i)
    fd(i)
    rt(90)
hideturtle()
done()