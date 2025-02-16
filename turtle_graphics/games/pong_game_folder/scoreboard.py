from turtle import *
class Scoreboard(Turtle):
    def __init__(self,screen_height) :
        super().__init__()
        self.screen_height = screen_height
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(x = -100, y = self.screen_height // 2 - 105 )
        self.write(self.l_score, align = "center", font = ("Courier", 80, "normal"))
        self.goto(x = 100, y = self.screen_height // 2 - 105 )
        self.write(self.l_score, align = "center", font = ("Courier", 80, "normal"))
        
    def update_score(self):
        self.clear()
        self.goto(x = -100, y = self.screen_height // 2 - 105 )
        self.write(self.l_score, align = "center", font = ("Courier", 80, "normal"))
        self.goto(x = 100, y = self.screen_height // 2 - 105 )
        self.write(self.l_score, align = "center", font = ("Courier", 80, "normal"))
    def l_score_increase(self):
        self.update_score()
    def r_score_increase(self):
        self.update_score()
