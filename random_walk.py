import turtle as t
from random import choice, randint


tim = t.Turtle()
t.colormode(255)
tim.pensize(15)
tim.speed(0)

directions = [0, 90, 180, 270]

def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  random_color = (r, g, b)
  return random_color

for i in range(1000):
  tim.color(random_color())
  tim.forward(30)
  tim.setheading(choice(directions))


# screen = Screen()
# screen.exitonclick()