import random
from turtle import *
def main():
    timmy = Turtle()
    screen = Screen()
    screen.colormode(255)
    screen.setup(1000,1000)
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    directions = [0,90,180,270]
    timmy.width(7)
    timmy.speed("fastest")
    timmy.hideturtle()
    for i in range(200):
        timmy.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        timmy.setheading(random.choice(directions))
        timmy.tiltangle(random.randint(0,360))
        timmy.forward(30)
    screen.exitonclick()
    
if __name__ == "__main__":
      main()
        