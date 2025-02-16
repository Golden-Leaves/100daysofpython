from turtle import *
class Player(Turtle):
    def __init__(self,screen_width, screen_height) :
        super().__init__()
        self.turtle_position = (0,(screen_height // 2 *-1) + 20)
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("purple")
        self.movement_distance = 10
        self.goto(x = self.turtle_position[0], y = self.turtle_position[1])
    def up(self):
        self.goto(x = self.xcor(), y = self.ycor() + self.movement_distance)
    def reset_position(self):
        self.goto(x = self.turtle_position[0], y = self.turtle_position[1])
