import turtle # import the module
from turtle import Turtle, Screen  # from the turtle module import the turtle class
# print(turtle, turtle.Turtle())


timmy = Turtle()  # create timmy object
print(timmy)
timmy.shape('turtle')
timmy.color('Red')
timmy.speed(10)

for loop in range(36):
    timmy.forward(100)
    timmy.left(100)
    timmy.circle(90, 90)



my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()  # continue on running
