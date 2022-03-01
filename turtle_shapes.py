import turtle
import math

def square(t, length, nbr_range):
    for i in range(nbr_range):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n, angle=360):
    degree = 360/n
    for i in range(int(n * (angle / 360))):
        t.fd(length)
        t.lt(degree)

def spirograph(t, length, n):
    degree = 360/n
    for i in range(int(degree - 1)):
        t.fd(length)
        t.lt(degree + 1)

def circle(t, r, length):
    circumfrence = 2 * math.pi * r
    n = circumfrence / length
    polygon(t, length, n)

def arc(t, r, length, angle):
    circumfrence = 2 * math.pi * r
    n = circumfrence / length
    polygon(t, length, n, angle)


bob = turtle.Turtle()

arc(bob, 150, 3, 270)

turtle.mainloop()