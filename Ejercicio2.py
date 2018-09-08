
#coding: utf-8

#In[2]:


import turtle
t = turtle.Pen()
turtle.resizemode("auto")   
t.speed=1
lpp=50
lpg=3*lpp
#print("Numero de lados del poligono grande")
#n=int(input())
n=4
h=float(0)
print("Numero de lados del poligono peque")
m=int(input())
t.speed=1
for h in range(0,n):
    t.penup()
    ang=h*(360/n)
    t.seth(ang)
    t.forward(lpg)
    t.seth(270)
    for k in range(0,m):
        t.pendown()
        angl=k*(360/m)
        t.seth(angl)
        t.forward(lpp)
        k=k+1
    h=h+1
t.hideturtle()                               
turtle.done()
turtle.bye()
                





