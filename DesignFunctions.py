def polygon(t, dist, sides):
    angle = 360/sides
    for times in range(sides):
        t.forward(dist)
        t.left(angle)

def triangle(t, dist):
    for times in range(3):
        t.forward(dist)
        t.left(120)

def square(t, dist):
    for times in range(4):
        t.forward(dist)
        t.left(90)

def jump(t,x,y):
  t.penup()
  t.goto(x,y)
  t.pendown()

def triangularspiral(t,times):
  for times in range(150): #triangularspiral
    t.begin_fill()
    polygon(t,times+.01,3)
    t.forward(times+4)
    t.left(47)
    t.forward(times+1)
    t.color(5,times+90,times+90)
    t.end_fill()
    
def triangularspiral2(t,times):
  for times in range(150): #triangularspiral
    t.begin_fill()
    polygon(t,times+.01,3)
    t.forward(times+4)
    t.left(47)
    t.forward(times+1)
    t.color(255,0,times+3)
    t.end_fill()

def triangledesign(t,r,g,b,times):
    for times in range(times): #triangulardesign
        g=times+1
        t.color(r,g,b)
        t.forward(times+3)
        t.right(118)

def trianglegradient(t,r,g,b,times):
    for times in range(times): #triangulardesign
        g=times+1
        t.color(r,g,b)
        t.forward(times+7)
        t.right(120)
