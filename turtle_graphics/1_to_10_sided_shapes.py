from turtle import *
import random
def turn_back():
    timmy.right(90)
    timmy.right(90)
def draw_square():
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)
    
timmy = Turtle()
screen = Screen()
screen.setup(1000,700)
timmy.shape("turtle")
timmy.color("dark magenta","lime")
def draw_shape(num_of_sides):
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    angle = 360 / num_of_sides
    timmy.pencolor(random.choice(colors))
    for i in range(num_of_sides):
        timmy.forward(100)
        timmy.right(angle)
    
try:
    number_of_sides = int(input("Enter the maximum amount of sides (Cannot be lower than 3): "))  
    if number_of_sides >= 3: 
      for n in range(3,number_of_sides + 1):
        draw_shape(n)
    else:
      print("Invalid input")
except ValueError:
    print("Invalid input.")

screen.exitonclick()
