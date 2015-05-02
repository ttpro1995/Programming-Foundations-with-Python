import turtle

def draw_square(meow):  # declare function to draw square
   
    meow.forward(200)     # move 100 distance
    meow.right(90)         # turn 90 degree
    meow.forward(200)
    meow.right(90)
    meow.forward(200)
    meow.right(90)
    meow.forward(200)
    meow.right(90)
    meow.right(5)
    
playground=turtle.Screen() # provide a windows for turtle to draw
playground.bgcolor("red") # change background color    
meow=turtle.Turtle() # meow = new turtle
meow.color("yellow")  # set color of turtle
meow.shape("turtle")  # set arrow shape to turtle

for i in range(0,72):
    draw_square(meow)


playground.exitonclick() # click any where to exit