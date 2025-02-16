import time
from turtle import *

class Snake:
    def __init__(self):
        self.turtle_distance = 20
        self.segments = []
        self.movement_speed = 20
        self.create_snake()
    def create_snake(self):
        for _ in range(3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x=self.turtle_distance, y=0)
            self.segments.append(new_segment)
            self.turtle_distance -= 20
    def extend(self,position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(x=self.turtle_distance, y=0)
        self.segments.append(new_segment)
        self.segments[-1].goto(position)
    
    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        
        self.create_snake()

    def move(self):
        
            for segment_number in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[segment_number - 1].xcor()
                new_y = self.segments[segment_number - 1].ycor()
                self.segments[segment_number].goto(x=new_x, y=new_y)
            self.segments[0].forward(self.movement_speed)
    def up(self):
        if self.segments[0].heading() != 270:
          self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading() != 90:
          self.segments[0].setheading(270)
    def left(self):
        if self.segments[0].heading() != 0:
          self.segments[0].setheading(180)
    def right(self):
        if self.segments[0].heading() != 180:
          self.segments[0].setheading(0)



