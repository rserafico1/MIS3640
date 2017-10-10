#3 
#The Drunkard’s Walk. 
#A drunkard in a grid of streets randomly picks one of four directions and stumbles to the next intersection, then again randomly picks one 
#of four directions, and so on. You might think that on average the drunkard doesn’t move very far because the choices cancel each other out,
#but that is actually not the case. Write a function to calculate the distance after n intersections.

#4 Use Turtle to draw the drunkard's walk in #3.

#Works with 'Terminal', rather than 'Debug Console' 

# INSTRUCTIONS
# 1. Run program on Terminal (make sure turtle window does not fully cover Terminal of 
#    Studio code because input in Terminal will be needed)
# 2. After list of coordinates will print, do not exit from drunkard's walk on Turtle
# 3. Go back to terminal and enter the last 'x' coordinate
# 4. Next, enter the last 'y' coordinate
# 5. It will then state "The drunkard started from (0,0) 
#    After 20 intersections, he's ____ blocks from where he started."

# Example of instructions of 3-5:
# Walked to: (-1,4)
# ... (other coordinates)...
# Walked to: (5,-1)
# Walked to: (5,-2)
# Walked to: (5,-1) ***this is the last coordinate
# Please enter last x coordinate: 5 ***input needed
# Please enter last y coordinate: -1 ***input needed 
# The drunkard started from (0,0).
# After 20 intersections, he's 5.0990195135927845 blocks from where he started.

import random
import turtle
import math
drunkard = turtle.Turtle()

def drunkard_walk(x, y, n):
    x = 0  #Origin (0,0)
    y = 0  #Origin (0,0)
    directions = ['N', 'S', 'E', 'W']  #Four options/directions 
    for blocks in range(n): 
        a = random.choice(directions)  #Picking a direction at random
        if a == 'N': #North
            y += 1
            print('Walked to: ({},{})'.format(x,y))  
            drunkard.setheading(90) #Setting the orientation of the turtle to 90 degrees (North)
        elif a == 'S': #South
            y -= 1
            print('Walked to: ({},{})'.format(x,y))
            drunkard.setheading(270) #Setting the orientation of the turtle to 270 degrees (South)
        elif a == 'E': #East
            x += 1
            print('Walked to: ({},{})'.format(x,y))
            drunkard.setheading(0) #Setting the orientation of the turtle to 0 degrees (East)
        else: #West                                              
            x -= 1
            print('Walked to: ({},{})'.format(x,y))
            drunkard.setheading(180) #Setting the orientation of the turtle to 180 degrees (West)
        drunkard.forward(50) #Moving the turtle forward by 50 (length of the lines in turtle)
    
drunkard_walk(0,0,20)

distance = drunkard_walk(0, 0, 20)
n = 20
x_2 = int(input("Please enter last x coordinate:")) #last x coordinate needed in order to calculate distance
y_2 = int(input("Please enter last y coordinate:")) #last y coordinate needed in order to calculate distance
xx = (x_2 - 0)**2 #last x cordinate & starting x coordinate in partial equation of distance formula
yy = (y_2 - 0)**2 #last y cordinate & starting y coordinate in partial equation of distance formula
distance = math.sqrt(xx + yy) 

print("The drunkard started from (%d,%d)." % (0, 0))
print("After", n, "intersections, he's", distance, "blocks from where he started.")

turtle.mainloop()
