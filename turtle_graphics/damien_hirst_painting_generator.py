from turtle import *
import random
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
def main():
    tim = Turtle()
    screen = Screen()
    screen.colormode(255)
    screen.setup(850,600)
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    tim.setheading(215)
    tim.forward(350)
    tim.setheading(0)  
    for i in range(1,11):
        for k in range(10):
          tim.pendown()
          tim.dot(25,random.choice(color_list))
          tim.penup()
          tim.forward(70)
        if i % 2 == 0:
            tim.penup()
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(0)
            tim.forward(70)
        elif i % 2 != 0:
            tim.penup()
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(70)
            



    screen.exitonclick()
if __name__ == "__main__":
    main()
    