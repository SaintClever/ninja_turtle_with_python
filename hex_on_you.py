from turtle import Turtle, Screen
from random import choice


tim = Turtle()

# for move in range(3):
#   tim.right(360 / 3)
#   tim.forward(100)

# for move in range(4):
#   tim.right(360 / 4)
#   tim.forward(100)

# for move in range(5):
#   tim.right(360 / 5)
#   tim.forward(100)

# for move in range(6):
#   tim.right(360 / 6)
#   tim.forward(100)

# for move in range(7):
#   tim.right(360 / 7)
#   tim.forward(100)


def draw(num_sides):
  colors = choice(['blue', 'brown', 'coral', 'cyan', 'Darkgrey', 'DarkRed', 'DarkGreen', 'DarkViolet', 'red', 'blue'])
  for i in range(num_sides):
    tim.color(colors)
    tim.right(360 / num_sides)
    tim.forward(100)

for i in range(3, 11):
  draw(i)
  


screen = Screen()
screen.exitonclick()