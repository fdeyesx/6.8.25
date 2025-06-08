from turtle import *
tracer(0)
left(90)
screensize(5000,5000)
k = 100

right(30)
for i in range(18):
    forward(11*k)
    right(120)
    forward(11*k)
    right(60)

up()
for x in range(0,20):
    for y in range(-15,20):
        goto(x*k,y*k)
        dot(5)
goto(0,0)
dot(7,'red')
done()
