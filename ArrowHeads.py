import turtle
from DesignFunctions import *
turtle.colormode(255)
bob = turtle.Turtle()
bob.speed(0)
#penup() - lifts the pen off the canvas
#pendown() - places back down on the canvas
#bob.goto(x,y) - places the pen on a coordinate

# vvv Creates a black background
bob.penup()
bob.goto(-1000,-1000)
bob.pendown()
bob.color(0,0,0)
bob.begin_fill()
polygon(bob,10000,4)
bob.end_fill()

bob.goto(0,-73)

trianglegradient(bob,255,0,255,250)#main design
jump(bob,0,-73)
triangledesign(bob,255,0,255,155) # spiral on top of main design
bob.setheading(180) # sets angle 
jump(bob,5,73)
trianglegradient(bob,255,127,0,250)
jump(bob,5,73)
triangledesign(bob,255,127,0,155)

jump(bob,-300,-73)
bob.setheading(0)

trianglegradient(bob,127,0,150,250)
jump(bob,-300,-73)
triangledesign(bob,127,0,150,155)
bob.setheading(180)
jump(bob,-295,73)
trianglegradient(bob,0,255,127,250)
jump(bob,-295,73)
triangledesign(bob,0,255,127,155)

jump(bob,300,-73)
bob.setheading(0)

trianglegradient(bob,0,153,0,250)
jump(bob,300,-73)
triangledesign(bob,0,153,0,155)
bob.setheading(180)
jump(bob,305,73)
trianglegradient(bob,178,255,102,250)
jump(bob,305,73)
triangledesign(bob,178,255,102,155)
