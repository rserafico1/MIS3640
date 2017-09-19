import turtle

rey = turtle.Turtle()

print(rey)

def polygon(t, length, n): 
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

import math 

def circle_a(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle_a(rey, 100)

rey.up()
rey.setposition(0,-200)
rey.down()

def circle_b(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle_b(rey, 100)

rey.up()
rey.setposition(200,-200)
rey.down()

def circle_c(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle_c(rey, 100)

rey.up()
rey.setposition(4,12)
rey.down()

def circle1(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle1(rey, 28)

rey.up()
rey.setposition(60,73)
rey.down()

def circle2(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle2(rey, 28)

rey.up()
rey.setposition(-52,74)
rey.down()

def circle3(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle3(rey, 28)

rey.up()
rey.setposition(5,130)
rey.down()

def circle4(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle4(rey, 28)

rey.up()
rey.setposition(210,-70)
rey.down()

def circle5(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle5(rey, 14)

rey.up()
rey.setposition(210,-160)
rey.down()

def circle6(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle6(rey, 14)

def polyline(t, n, length, angle):
  for i in range(n):
      t.fd(length)
      t.lt(angle)

rey.up()
rey.setposition(-45,12)
rey.down()


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
    rey.left(90)

polygon(rey, 3, 100)

rey.up()
rey.setposition(90,50)
rey.down()

def polygon2(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

polygon2(rey, 3, 100)


rey.up()
rey.setposition(5,100)
rey.left(330)
rey.down()


def polygon3(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

polygon3(rey, 3, 100)

rey.up()
rey.setposition(-80,50)
rey.left(330)
rey.down()


def polygon4(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

polygon4(rey, 3, 100)

rey.up()
rey.setposition(200, -100)
rey.left(330)
rey.down()

def arc1(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length /n 
    step_angle = angle/n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc1(rey, 50, 180)

rey.up()
rey.setposition(200, -100)
rey.left(360)
rey.down()

def arc2(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length /n 
    step_angle = angle/n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc2(rey, 50, 180)

rey.up()
rey.setposition(200, -100)
rey.left(360)
rey.down()

def arc2(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length /n 
    step_angle = angle/n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc2(rey, 50, 180)

def draw_petal(t, r, angle):
    arc2(t, r, angle)
    rey.left(180-angle)
    arc2(t, r, angle)
    rey.left(180-angle)

#draw_petal(rey, 100, 100)

rey.up()
rey.setposition(5,-100)
rey.down()

def draw_flower(t, petals, r, angle):
    for petal in range(petals):
        draw_petal(t, r, angle)
        rey.left(360/petals)

draw_flower(rey, 6, 120, 50) 

turtle.mainloop()