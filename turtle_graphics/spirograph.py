from turtle import *
import random
def main(number_of_gaps):
    timmy = Turtle()
    screen = Screen()
    screen.setup(700,500)
    timmy.width(2)
    screen.colormode(255)
    timmy.speed("fastest")
    timmy.hideturtle()
    for i in range(int(360 / number_of_gaps)):
        timmy.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        timmy.circle(100)
        timmy.setheading(timmy.heading() + number_of_gaps)
    screen.exitonclick()
if __name__ == "__main__":
    main(10)
    