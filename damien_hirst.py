import turtle, colorgram
from turtle import Screen
from random import choice


colors = colorgram.extract('assets/damien_hirst.jpg', 17)

tuple_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
# tuple_colors = [(color.rgb[0], color.rgb[1], color.rgb[2]) for color in colors]
print(tuple_colors[3:]) # remove the first 3 tuples because colors are too light
colors = tuple_colors[3:]

turtle.colormode(255)
tim = turtle.Turtle()
tim.speed(0)
tim.hideturtle()
tim.penup()

x = -330
y = -300

user_input = int(input('What dot size do you want [1 - 100]: '))

while y <= 300:
  tim.goto(x, y)
  for color in colors:
    random_color = choice(colors)
    x = -330
    tim.dot(100, random_color)
    tim.forward(50)
  print(x, y)
  y += 50

screen = Screen()
# print(screen.screensize())
screen.exitonclick()