import turtle

rey = turtle.Turtle()

print(rey)

def square(t, length): 
    for i in range(4):
        t.fd(length)
        t.lt(90)

#square(rey, 250)

def polygon(t, length, n): 
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

#polygon(rey, 50, 8)



import math 

rey.up()
rey.setposition(0,-200)
rey.down()

def circle_b(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle_b(rey, 100)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length /n 
    step_angle = angle/n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

#arc(rey, 100, 180)

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle."""
    for i in range(n):
        t.fd(length)
        t.lt(angle)
        
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

#polygon(rey, 4, 100)


def arc2(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length /n 
    step_angle = angle/n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

#arc2(rey, 50, 180)

turtle.mainloop()
