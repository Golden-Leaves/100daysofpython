from turtle import *
import random
class Ball(Turtle):
    def __init__(self,screen_width,screen_height,ball_speed):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball_speed_x = ball_speed
        self.ball_speed_y = ball_speed
        self.sleep_value = 0.05
        self.color("white")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid = 1, stretch_len = 1)
        self.speed(2)
        self.goto(x = 0 , y = 0)

    def move(self):
        self.goto(x = self.xcor() + self.ball_speed_x, y = self.ycor() + self.ball_speed_y)
    def bounce_y(self):
        self.ball_speed_y *= -1
        self.sleep_value *= 0.9
    def bounce_x(self):
        self.ball_speed_x *= -1
        self.sleep_value *= 0.9
    def reset_position(self):
        self.goto(x = 0, y = 0)
        self.bounce_x()
        self.sleep_value = 0.05

        