import turtle
#Haha TTpro
def draw_triangle(the_turtle,length,ori,recursion):
    recursion=recursion+1
    meow= the_turtle

    for i in range(0,3):
        if(recursion<4):
        #if (0):
            meow.forward(length/2)
            meow.left(120)
            draw_triangle(meow,length/2,0,recursion)
            meow.right(120)
            meow.forward(length/2)
        else:
            meow.forward(length)
        if (ori==1):
            meow.left(120)
        else:
            meow.right(120)

meow = turtle.Turtle() # init
meow.speed(10) # speed = 1 to slow turtle down
meow.color("yellow","green") # set color5
meow.shape("turtle") # set shape to a turtle
background = turtle.Screen()  # create background
background.bgcolor("red")     # set background color to red


draw_triangle(meow,200,1,0)

#meow.forward(100)
#meow.left(120)
#draw_triangle(meow,100,0,0)
#meow.right(120)

background.exitonclick()      # click anywhere to close background