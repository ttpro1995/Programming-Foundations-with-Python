import turtle
#HahaTTpro
def draw_square():  # declare function to draw square
    playground=turtle.Screen() # provide a windows for turtle to draw
    playground.bgcolor("pink") # change background color
    meow=turtle.Turtle() # meow = new turtle
    meow.color("yellow")  # set color of turtle
    meow.shape("turtle")  # set arrow shape to turtle
    meow.speed(1)        
    meow.forward(200)     # move 100 distance
    meow.right(90)         # turn 90 degree
    meow.forward(200)
    meow.right(90)
    meow.forward(200)
    meow.right(90)
    meow.forward(200)
    meow.right(90)
    playground.exitonclick() # click any where to exit
    
draw_square()  # run function draw_square
