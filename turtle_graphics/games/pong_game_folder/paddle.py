from turtle import *
class Paddle(Turtle):
    def __init__(self,screen_width,position,paddle_speed):
        super().__init__()
        self.paddle_speed = paddle_speed
        self.position = position
        self.screen_width = screen_width
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.goto(x = position , y = 0)
    def go_up(self):
        self.goto(self.xcor() , y = self.ycor() + self.paddle_speed)
    def go_down(self):
        self.goto(self.xcor() , y = self.ycor() - self.paddle_speed)


