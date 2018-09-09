
# coding: utf-8
import turtle,math
def regular_shape(aturtle, radius, sides):
    c = 2 * math.pi * radius
    cs = c / m
    asp = 360.0 / m 
    for x in range(m):
        t.seth(0)
        t.left(asp*x)
        t.forward(cs)
t = turtle.Pen()
turtle.resizemode("auto")   
t.speed=1
lpp=15
print("Numero de filas")
n=int(input())
h=float(0)
#print("Numero de lados del poligono de la base")
circumference = 2 * math.pi * lpp
m=n+2
s=n
l=1
t.speed=7
while (l<=s):
    for h in range(0,n):
        t.pendown()
        regular_shape(turtle.Turtle(),lpp,m)
        t.seth(0)
        t.penup()
        t.forward(125)
    n=n-1
    m=m-1
    t.goto(0,0)
    t.seth(60)
    t.forward(l*125)
    l=l+1
t.hideturtle()                   
turtle.done()
turtle.bye()
                





