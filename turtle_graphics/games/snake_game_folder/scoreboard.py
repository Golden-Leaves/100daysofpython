from turtle import *
import os
class ScoreBoard(Turtle):
    def __init__(self,screen_height):
        super().__init__()
        try:
            with open("snake_game_high_score.txt","r") as f:
                content = f.read().strip()
                if content.isdigit():
                    self.high_score = int(content)
                else:
                    self.high_score = 0
        except IOError or FileNotFoundError:
            with open("snake_game_high_score.txt","w") as f:
                f.write("0")
            self.high_score = 0
                
        self.score = 0
        self.screen_height = int(screen_height)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x = 0, y = (self.screen_height // 2) - 35) # Subtracted by 30 to prevent cliping the edge
        self.write(f"Score: {self.score}" f" High Score: {self.high_score}", align = "center", font = ("Arial",24,"normal"))


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}" f" High Score: {self.high_score}", align = "center", font = ("Arial",24,"normal"))
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("snake_game_high_score.txt","w") as f:
            f.write(str(self.high_score))
        self.score = 0
        self.update_score()
        


        