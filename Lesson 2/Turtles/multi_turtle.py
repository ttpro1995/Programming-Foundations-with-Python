import turtle

meow=turtle.Turtle()
meow.shape("turtle")
woof = turtle.Turtle()
woof.shape("turtle")
meow.color("red")
woof.color("blue")
meow.speed(1)
woof.speed(1)
background = turtle.Screen()
woof.forward(100)
meow.right(90)
meow.forward(50)
meow.forward(200)     # move 100 distance
meow.right(90)         # turn 90 degree
meow.forward(200)
meow.right(90)
meow.forward(200)
meow.right(90)
meow.forward(200)
meow.right(90)

woof.left(90)
woof.forward(100)
background.exitonclick()
