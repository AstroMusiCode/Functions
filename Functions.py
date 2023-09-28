import turtle
import math
import numpy

t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.penup()

def parabola(x,y, a, b, c, d, domain, power):
    x1 = x
    y1 = y
    i = 0
    while (i < (domain+1)):
        y1 = a*(math.pow((b*(x1-c)), power))+d
        t.pendown()
        t.setposition(x1,y1)
        t.penup()
        x1+=1
        i+=1
    t.penup()
    x1 = 0
    y1 = 0
    t.setposition(x1, y1)
    i = 0
    while (i < (domain+1)):
        y1 = a*(math.pow(b*(x1-c), power))+d
        t.pendown()
        t.setposition(x1,y1)
        t.penup()
        x1-=1
        i+=1


x = 0
y = 0

a = float(input("Vertical Dilation: "))
b = float(input("Horizontal Dilation: "))
c = float(input("Horizontal Shift: "))
d = float(input("Vertical Shift: "))
domain = float(input("Domain: "))
exponent = float(input("Exponent (>0 only): "))

parabola(x, y, a, b, c, d, domain, exponent)

input()