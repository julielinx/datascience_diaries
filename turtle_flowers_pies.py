from re import A
import turtle
import math

def turtle_pie(t, n, r):
    a = 360/n
    b = (180 - a) / 2
    turn = 180 - b
    base = 2 * r * math.sin(math.radians(a/2))
    for i in range(n):
        t.fd(r)
        t.lt(turn)
        t.fd(base)
        t.lt(turn)
        t.fd(r)
        t.lt(180)

def turtle_pie2(t, n, length):
    a = 360/n
    b = (180 - a) / 2
    base = length / 2
    r = base / (2 * math.sin(math.radians(a/2)))
    turn = 180 - b
    for i in range(n):
        t.fd(r)
        t.lt(turn)
        t.fd(base)
        t.lt(turn)
        t.fd(r)
        t.lt(180)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    circumfrence = 2 * math.pi * r
    arc_length = circumfrence * (angle / 360)
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)

def turtle_flower(t, n, r):
    a = 360/n
    b = 180 - a
    for i in range (n):
        arc(t, r, a)
        t.lt(b)
        arc(t, r, a)
        t.lt(180)

bob = turtle.Turtle()
# turtle.speed(1)
# turtle.delay(100)
# turtle_pie(bob, 5, 50)
# turtle_pie2(bob, 13, 50)
turtle_flower(bob, 13, 150)
# arc(bob, 150, (360/7))

turtle.mainloop()


['INTERVAL-CASE_CUSTOMER_START_INTRVL', 'INTERVAL-CASE_CUSTOMER_END_INTRVL', 'INTERVAL-CASE_ASSET_START_INTRVL',
'INTERVAL-CASE_ASSET_END_INTRVL', 'INTERVAL-CASE_INCIDENT_START_INTRVL', 'INTERVAL-CASE_ASSET_FAILURE_INTRVL']

['I-CASE_CUSTOMER_START_INTRVL', 'I-CASE_CUSTOMER_END_INTRVL', 'I-CASE_ASSET_START_INTRVL',
'I-CASE_ASSET_END_INTRVL', 'I-CASE_INCIDENT_START_INTRVL', 'I-CASE_ASSET_FAILURE_INTRVL']

# More re: turtles: https://www.geeksforgeeks.org/draw-ellipse-using-turtle-in-python/