# This project is playing around with graphics in python 
# and practicing how to use functions 


def print_triangular_numbers(n):
          i=1
          while i <= n:
                    print (i, i*(i+1)/2,"\t")
                    i+=1
                    
print(print_triangular_numbers(5))
                    

# each step is random 

# import necessary packages
import time
import random
import turtle

def isInScreen(w, t):
    if random.random() > 0.1:
        return True
    else:
        return False

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')

while isInScreen(wn, t):
    coin = random.randrange(0, 2)
    rand=random.randrange(0,390)
    if coin == 0:              
        t.left(rand)
    else:                      
        t.right(rand)

    t.forward(50)

time.sleep(1)
wn.clearscreen()  


## create two turtles each with a random starting location.
##Keep the turtles moving until one of them leaves the screen.

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t1, t2 = turtle.Turtle(), turtle.Turtle()
t1.speed(0)
t2.speed(0)
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('turtle')
t2.color('blue')
wn.bgcolor('lightgreen')

#We set our random initial position
for t in (t1, t2):
    t.penup()
    xinit = random.randrange(0, wn.window_width())
    xinit -= wn.window_width() / 2
    yinit = random.randrange(0, wn.window_height())
    yinit -= wn.window_height() / 2
    
    t.setx(xinit)    
    t.sety(yinit)
    t.pendown()

while isInScreen(wn, t1) and isInScreen(wn,t2):
    for t in (t1, t2):
        coin = random.randrange(0, 2)
        rand = random.randrange(0,90)
        if coin == 0:
            t.left(rand)
        else:
            t.right(rand)

    t1.forward(10)
    t2.forward(10)

    if not (isInScreen(wn,t1) or isInScreen(wn,t2)):  ##stops the program until one of the turtles leaves the screen
              break

time.sleep(1)
wn.clearscreen()  

##Make the turtle turn around when it hits the wall or when
##one turtle collides with another turtle 
# (when the positions of the two turtles are closer than some small number)

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        stillIn = False
    if turtleY > topBound or turtleY < bottomBound:
        stillIn = False

    return stillIn

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.speed(10)
t2.speed(10)
wn = turtle.Screen()

t1.shape('turtle')
t2.shape('turtle')
t2.color('blue')
wn.bgcolor('lightgreen')


# random intinial point
for t in (t1, t2):
    t.penup()
    xinit = random.randrange(0, wn.window_width())
    xinit -= wn.window_width() / 2
    yinit = random.randrange(0, wn.window_height())
    yinit -= wn.window_height() / 2
    
    t.setx(xinit)    
    t.sety(yinit)
    
    t.pendown()
    
while isInScreen(wn, t1) or isInScreen(wn,t2):
    for t in (t1, t2):
        coin = random.randrange(0, 2)
        rand= random.randrange(0,90)
        if coin == 0:
            t.left(rand)
        else:
            t.right(rand)

    t1.forward(10)
    t2.forward(10)

    if t1.distance(t2) > 360 and t1.distance(t2) < 0.001:
              t1.setpos(random.randrange(wn.window_height(), wn.window_width()))

leftBound=-50
bottomBound=-50
rightBound=50
topBound=50
wn.setworldcoordinates(leftBound,bottomBound,rightBound,topBound)
while True:
          
          turtle1 = t1.xcor()
          turtle2 = t1.ycor()
          turtle3 = t2.xcor()
          turtle4 = t2.ycor()
          
          if turtle1 >= rightBound and turtle1 <= topBound:
                  stillIn = t1.heading()
                  t1.setheading(180-stillIn)
          if turtle2 > leftBound and turtle2 > bottomBound:
                  stillIn = t1.heading()
                  t1.setheading(-stillIn)
          if turtle3 >= rightBound and turtle3 > topBound:
                  stillIn = t2.heading()
                  t2.setheading(180-stillIn)
          if turtle4 > leftBound and turtle4 > bottomBound:
                  stillIn = t2.heading()
                  t2.setheading(-stillIn)
          t1.fd(1)
          t2.fd(1)
        
                    
time.sleep(1)
wn.clearscreen()  


