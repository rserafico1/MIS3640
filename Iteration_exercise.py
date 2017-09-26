import math

def mysqrt(a):
    x = 3
    while True:
        y = (x + (a/x)) / 2
        if abs(y-x)< 0.0000001:
            break
        x = y
    return x

def test_square_root():
    a = 0
    while a < 10:
        q = mysqrt(a)
        r = math.sqrt(a)
        d = abs(q-r)
        a += 1
        print (a)
        print (q)
        print (r)
        print (d)
        
test_square_root()
