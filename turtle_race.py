import turtle
import time
import math
from turtle import *
from random import randint

turtle.setup(1000,800)
turtle.bgcolor('forestgreen')
turtle.hideturtle()


#Track outline drawing with a color fill
track = turtle.Turtle()
track.speed(0)
track.penup()
track.setpos(-180,310)
track.pendown()
track.showturtle()
track.fillcolor('dark grey')
track.begin_fill()
track.forward(300)
for z in range(180):
    track.forward(4)
    track.right(1)
track.forward(300)
for z in range(180):
    track.forward(4)
    track.right(1)
track.end_fill()
track.hideturtle()

#Track inline drawing with a color fill
track.penup()
track.setpos(-180, 200)
track.pendown()
track.showturtle()
track.fillcolor('brown')
track.begin_fill()
track.forward(300)
for x in range(180):
    track.forward(2)
    track.right(1)
track.forward(300)
for x in range(180):
    track.forward(2)
    track.right(1)
track.end_fill()
track.hideturtle()


#Start/finish line
startline = turtle.Turtle()
stamp_size = 20
square_size = 5
finish_line = -20

startline.color('black')
startline.shape('square')
startline.shapesize(square_size / stamp_size)
startline.penup()

for i in range(12):
    startline.setpos(finish_line, (-32 - (i * square_size * 2)))
    startline.stamp()

for j in range(11):
    startline.setpos(finish_line + square_size, ((-32 - square_size) - (j * square_size * 2)))
    startline.stamp()

#MOTORCYCLE 1
motorcycle1 = turtle.Turtle()
motorcycle1.speed(0)
motorcycle1.penup()
motorcycle1.setpos(-40, -130)
motorcycle1.pendown()
motorcycle1.color('red')
motorcycle1.shape('turtle')

#MOTORCYCLE 2
motorcycle2 = turtle.Turtle()
motorcycle2.speed(0)
motorcycle2.penup()
motorcycle2.setpos(-40, -100)
motorcycle2.pendown()
motorcycle2.color('blue')
motorcycle2.shape('turtle')

#MOTORCYCLE 3
motorcycle3 = turtle.Turtle()
motorcycle3.speed(0)
motorcycle3.penup()
motorcycle3.setpos(-40, -70)
motorcycle3.pendown()
motorcycle3.color('yellow')
motorcycle3.shape('turtle')

#MOTORCYCLE 4
motorcycle4 = turtle.Turtle()
motorcycle4.speed(0)
motorcycle4.penup()
motorcycle4.setpos(-40, -40)
motorcycle4.pendown()
motorcycle4.color('green')
motorcycle4.shape('turtle')

#Making a countdown from 3 to 0 to be drawn on the inline of the track
def countdown(n) :
    while n > 0:
        write(n, font=('Arial', 40, 'bold'))
        time.sleep(1)
        clear()
        n = n - 1
        if n == 0:
            write('Go!', font=('Arial', 40, 'bold'))
            time.sleep(1)
            clear()
            
countdown(3)

#So now the racing starts
#I want to move the turtles with random speed at the 'straight parts'
for i in range(35):
    motorcycle1.forward(randint(1,9))
    motorcycle2.forward(randint(1,9))
    motorcycle3.forward(randint(1,9))
    motorcycle4.forward(randint(1,9))

#Turn left - I couldn't make them ride randomly
for j in range(180):
    motorcycle1.forward(3)
    motorcycle1.left(1)
    motorcycle2.forward(3)
    motorcycle2.left(1)
    motorcycle3.forward(3)
    motorcycle3.left(1)
    motorcycle4.forward(3)
    motorcycle4.left(1)

#Second straight part
for k in range(60):
    motorcycle1.forward(randint(1,9))
    motorcycle2.forward(randint(1,9))
    motorcycle3.forward(randint(1,9))
    motorcycle4.forward(randint(1,9))

#Second left turn
for l in range(180):
    motorcycle1.forward(3)
    motorcycle1.left(1)
    motorcycle2.forward(3)
    motorcycle2.left(1)
    motorcycle3.forward(3)
    motorcycle3.left(1)
    motorcycle4.forward(3)
    motorcycle4.left(1)

#Riding straight to the finish line
for m in range(35):
    motorcycle1.forward(randint(1,9))
    motorcycle2.forward(randint(1,9))
    motorcycle3.forward(randint(1,9))
    motorcycle4.forward(randint(1,9))

turtle.done()
