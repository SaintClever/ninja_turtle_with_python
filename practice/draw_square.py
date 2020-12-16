from turtle import Turtle, Screen
# import heroes, villains


# print(heroes.gen(), villains.gen())

tim = Turtle()

for move in range(4):
    tim.forward(100)
    tim.left(90)


screen = Screen()
screen.exitonclick()

