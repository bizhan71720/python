import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')
rotate=int(360)
def drawCicles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawCicles(t,size)
        t.right(360/repeat)
drawSpecial(Albert,100,10)
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
rotate=int(90)
def drawCicles(t,size):
    for i in range(12):
        t.circle(size)
        size=size-8
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawCicles(t,size)
        t.right(360/repeat)
drawSpecial(Steve,100,10)
b = turtle.Turtle()
b.speed(0)
b.color('blue')
rotate=int(80)
def drawCicles(t,size):
    for i in range(7):
        t.circle(size)
        size=size-6
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawCicles(t,size)
        t.right(360/repeat)
drawSpecial(b,100,10)
c = turtle.Turtle()
c.speed(0)
c.color('orange')
rotate=int(90)
def drawCicles(t,size):
    for i in range(12):
        t.circle(size)
        size=size-24
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawCicles(t,size)
        t.right(360/repeat)
drawSpecial(c,100,10)
d = turtle.Turtle()
d.speed(0)
d.color('pink')
rotate=int(90)
def drawCicles(t,size):
    for i in range(5):
        t.circle(size)
        size=size-17
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawCicles(t,size)
        t.right(360/repeat)
drawSpecial(d,100,10)

turtle.getscreen()._root.mainloop()