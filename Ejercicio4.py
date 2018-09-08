
# coding: utf-8

# In[ ]:

import turtle
t = turtle.Pen()
turtle.resizemode("auto")   
t.speed=1
lpp=50
lpg=3*lpp
print("Numero de filas")
n=int(input())
h=float(0)
print("Numero de lados del poligono de la base")
m=int(input())
t.speed=1
l=0
for l in range(0,n):
    for h in range(0,n):
        for k in range(0,m):
            t.pendown()
            angl=k*(360/m)
            t.seth(angl)
            t.forward(lpp)
            k=k+1
        t.penup()
        t.seth(0)
        t.forward(100)
        h=h+1
    l=l+1
    t.goto(0,0)
    t.seth(60)
    t.forward(l*100)
    t.pendown()
    s=s-1
    n=n-1
t.hideturtle()                   
turtle.done()
turtle.bye()