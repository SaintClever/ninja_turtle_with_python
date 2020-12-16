import turtle, colorgram
from turtle import Screen
from random import choice


colorgram_extract = colorgram.extract('assets/damien_hirst.jpg', 17)
tuple_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colorgram_extract]
# tuple_colors = [(color.rgb[0], color.rgb[1], color.rgb[2]) for color in colors]
# print(tuple_colors[3:]) # remove the first 3 tuples because colors are too light
colors = tuple_colors[3:]


turtle.colormode(255)
tim = turtle.Turtle()
tim.speed(0)
tim.hideturtle()
tim.penup()


x = -330
y = -300

user_input = int(input('Desired dot size [1 - 100]: '))

while y <= 300:
  tim.goto(x, y)
  counter = 0

  for color in colors:
    counter += 1
    random_color = choice(colors)
    # print(random_color)
    x = -330
    tim.dot(user_input, random_color)
    # print(counter, len(colors))
    if counter <= (len(colors) - 1): # This prevents an uneede forward step 50 pixels
      tim.forward(50)
      
  # print(x, y)
  y += 50


screen = turtle.Screen()
# print(screen.screensize())
screen.exitonclick()