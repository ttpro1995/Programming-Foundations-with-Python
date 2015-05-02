import turtle

def draw_square():  # declare draw_sqaure function
    meow = turtle.Turtle() # init a turtle named meow
    meow.color("yellow")   # set yellow to yellow
    meow.shape("turtle")   # set shape to turtle
    for i in range(0,4):   # for (int i =0, i<4;i++)
        meow.forward(100)  # move turtle forward 100 distance
        meow.right(90)     # turn right 90 degree
        # end for loop
#end draw_square function
    
def draw_triangle():
    meow = turtle.Turtle() # init
    meow.color("yellow")
    meow.shape("turtle")
    for i in range(0,3):
        meow.forward(100)
        meow.left(180-60)

def draw_circle():
    meow = turtle.Turtle() # init
    meow.color("yellow")
    meow.shape("turtle")
    meow.circle(100)       # draw a circle with radiun = 100
        
        
background = turtle.Screen()  # create background
background.bgcolor("red")     # set background color to red
draw_square()
draw_triangle()
draw_circle()
background.exitonclick()      # click anywhere to close background
