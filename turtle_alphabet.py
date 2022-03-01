import turtle
import math

lower_size = 10

def draw_a(t, r=lower_size):
    t.circle(r)
    t.pu()
    t.fd(r)
    t.lt(90)
    t.fd(r*2)
    t.lt(180)
    t.pd()
    t.fd(r*2)
    t.pu()
    t.lt(90)
    t.fd(r*2)
    t.pd()

def draw_b(t, r=lower_size):
    t.pu()
    t.forward(r)
    t.pd()
    t.circle(r)
    t.pu()
    t.forward(-r)
    t.lt(90)
    t.fd(r*4)
    t.lt(180)
    t.pd()
    t.fd(r*4)
    t.pu()
    t.lt(90)
    t.fd(r*4)
    t.pd()

def draw_c(t, r=lower_size):
    t.pu()
    t.fd(r)
    t.pd()
    t.circle(r, 60)
    t.pu()
    t.circle(r, 60)
    t.pd()
    t.circle(r, 240)
    t.pu()
    t.fd(r*2)
    t.pd()

def draw_d(t, r=lower_size):
    t.pu()
    t.fd(r)
    t.pd()
    t.circle(r)
    t.pu()
    t.fd(r)
    t.lt(90)
    t.fd(r*4)
    t.lt(180)
    t.pd()
    t.fd(r*4)
    t.pu()
    t.lt(90)
    t.fd(r*2)
    t.pd()

def draw_e(t, r=lower_size):
    t.pu()
    t.fd(-r)
    t.lt(90)
    t.fd(r)
    t.rt(90)
    t.pd()
    t.fd(r*2)
    t.lt(90)
    t.circle(r, 315)
    t.pu()
    t.circle(r, -45)
    t.fd(r*3)
    t.pd()

def draw_f(t, r=lower_size):
    t.lt(90)
    t.fd(r * 3)
    t.circle(-r, 180)
    t.pu()
    t.fd(r)
    t.rt(90)
    t.fd(r)
    t.pd()
    t.fd(r*2)
    t.pu()
    t.lt(90)
    t.fd(r*2)
    t.lt(90)
    t.fd(r*3)
    t.pd()

def draw_g(t, r=lower_size):
    t.circle(r)
    t.pu()
    t.fd(r)
    t.lt(90)
    t.fd(r)
    t.lt(180)
    t.pd()
    t.fd(r*2)
    t.circle(-r, 180)
    t.pu()
    t.fd(r)
    t.rt(90)
    t.fd(r*4)
    t.pd()

def draw_h(t, r=lower_size):
    t.lt(90)
    t.fd(r*4)
    t.fd(-r*3)
    t.circle(-r, 180)
    t.fd(r)
    t.pu()
    t.lt(90)
    t.fd(r*2)
    t.pd()

def draw_i(t, r=lower_size):
    t.lt(90)
    t.fd(r*2)
    t.pu()
    t.fd(r)
    t.pd()
    t.circle(r//10)
    t.pu()
    t.fd(-r*3)
    t.rt(90)
    t.fd(r*2)
    t.pd()

def draw_j(t, r=lower_size):
    t.pu()
    t.fd(r*2)
    t.rt(90)
    t.fd(-r*3)
    t.pd()
    t.circle(r//10)
    t.pu()
    t.fd(r)
    t.pd()
    t.fd(r*3)
    t.circle(-r, 180)
    t.pu()
    t.fd(r)
    t.rt(90)
    t.fd(r*4)
    t.pd()

def draw_k(t, r=lower_size):
    t.lt(90)
    t.fd(r*4)
    t.fd(-r*3)
    t.rt(45)
    t.fd(r*math.sqrt(2))
    t.fd(-r*math.sqrt(2))
    t.rt(90)
    t.fd(r*math.sqrt(2))
    t.fd(-r*math.sqrt(2))
    t.pu()
    t.rt(45)
    t.fd(r)
    t.lt(90)
    t.fd(r*3)
    t.pd()

def draw_l(t, r=lower_size):
    t.lt(90)
    t.fd(r*4)
    t.fd(-r*4)
    t.rt(90)
    t.pu()
    t.fd(r*2)
    t.pd()

def draw_m(t, r=lower_size):
    t.lt(90)
    t.fd(r*2)
    t.fd(-r)
    t.circle(-r, 180)
    t.fd(r)
    t.lt(180)
    t.fd(r)
    t.circle(-r, 180)
    t.fd(r)
    t.pu()
    t.lt(90)
    t.fd(r*2)
    t.pd()

def draw_n(t, r=lower_size):
    t.lt(90)
    t.fd(r*2)
    t.fd(-r)
    t.circle(-r, 180)
    t.fd(r)
    t.pu()
    t.lt(90)
    t.fd(r*2)
    t.pd()

def draw_o(t, r=lower_size):
    t.pu()
    t.fd(r)
    t.pd()
    t.circle(r)
    t.pu()
    t.fd(r*3)
    t.pd()

def draw_p(t, r=lower_size):
    t.pu()

def draw_q(t, r=lower_size):
    t.pu()

def draw_r(t, r=lower_size):
    t.pu()

def draw_s(t, r=lower_size):
    t.pu()

def draw_t(t, r=lower_size):
    t.pu()

def draw_u(t, r=lower_size):
    t.pu()

def draw_v(t, r=lower_size):
    t.pu()

def draw_w(t, r=lower_size):
    t.pu()

def draw_x(t, r=lower_size):
    t.pu()

def draw_y(t, r=lower_size):
    t.pu()

def draw_z(t, r=lower_size):
    t.pu()

bob = turtle.Turtle()

draw_a(bob)
draw_b(bob)
draw_c(bob)
draw_d(bob)
draw_e(bob)
draw_f(bob)
draw_g(bob)
draw_h(bob)
draw_i(bob)
draw_j(bob)
draw_k(bob)
draw_l(bob)
draw_m(bob)
draw_n(bob)
draw_o(bob)
# draw_p(bob)
# draw_q(bob)
# draw_r(bob)
# draw_s(bob)
# draw_t(bob)
# draw_u(bob)
# draw_v(bob)
# draw_w(bob)
# draw_x(bob)
# draw_y(bob)
# draw_z(bob)

turtle.mainloop()

# def talloval(r):               # Verticle Oval
#     turtle.left(45)
#     for loop in range(2):      # Draws 2 halves of ellipse
#         turtle.circle(r,90)    # Long curved part
#         turtle.circle(r/2,90)  # Short curved part

# def flatoval(r):               # Horizontal Oval
#     turtle.right(45)
#     for loop in range(2):
#         turtle.circle(r,90)
#         turtle.circle(r/2,90)

# From: https://stackoverflow.com/questions/29465666/how-do-you-draw-an-ellipse-oval-in-turtle-graphics-python