import turtle 

# Draw a line from(x1,y1) to (x2,y2)
def drawLine(x1,y1,x2,y2):
    turtle.penup()

    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2, y2)

#write a string s at the specified location (x, y)
def writeText (s,x,y):
    turtle.penup() # pull the pen up 
    turtle.goto(x,y)
    turtle.pendown() # pull the pen down 
    turtle.write(s) #write a string

#Draw a point at the specified location (x,y)
def drawPoint(x,y):
    turtle.penup() # pull the pen up 
    turtle.goto(x,y) 
    turtle.pendown() # Pull the pen down 
    turtle.begin_fill() #begin to fill color in a shape 
    turtle.circle(3)
    turtle.end_fill() #FILL THE SHAPE 

def drawcircle(x = 0, y = 0, radius = 10):
    turtle.penup()
    turtle.goto(x,y - radius)
    turtle.pendown() 
    turtle.circle(radius)

    def drawRectangle(x = 0, y = 0, width = 10, height = 10):
        turtle.penup()
        turtle.goto(x + width / 2, y + height / 2)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(width)
        turtle.penup()
        turtle.goto(x,y - radius)
        turtle.pendown()
        turtle.circle(radius)

        def drawRectangle(x = 0, y = 0, width = 10, height = 10):
         turtle.penup()
         turtle.goto(x + width / 2, y + height / 2)
         turtle.pendown()
         turtle.right(90)
         turtle.forward(height)
         turtle.right(90)
         turtle.forward(width)
         turtle.right(90)
         turtle.forward(height)
         turtle.right(90)
         turtle.forward(width)



            