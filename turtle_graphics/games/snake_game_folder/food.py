from turtle import *
import random
class Food(Turtle):
    def __init__(self,screen_width,screen_length):
        self.screen_width = int(screen_width)
        self.screen_length = int(screen_length)
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.refresh()

    def refresh(self):
        random_x = random.randint(int((self.screen_width // 2.1)) * -1, int(self.screen_width // 2.1)) #Added decimals to prevent food from clipping the edge
        random_y = random.randint(int(self.screen_length // 2.1) * -1, int(self.screen_length // 2.1))
        self.goto(x = random_x, y = random_y)
