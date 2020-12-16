from random import randint
from turtle import Screen
import turtle, Screen


tim = turtle.Turtle()
turtle.colormode(255)
direction = range(361)


draw_speed = int(input('Draw speed [1, 3, 6, 10, 0]: '))
user_input = int(input('Number of rings [1 to 8]: '))
circle_size = int(input('Circle size [1 to 500]: '))
pen_size = int(input('Pen size [1 to 100]: '))


for i in range(0, 361, user_input): # user_input to 8 is best
  rgb = (randint(0, 255), randint(0, 255), randint(0, 255))
  # print(rgb)
  tim.speed(draw_speed) 
  tim.color(rgb)
  tim.circle(circle_size) # circle equal 100 is the best
  tim.setheading(direction[i])
  # print(direction[i])
  tim.pensize(pen_size) # pensize equal to 1 is the best


screen = Screen()
screen.exitonclick()