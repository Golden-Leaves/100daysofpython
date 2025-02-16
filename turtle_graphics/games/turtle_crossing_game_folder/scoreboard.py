from turtle import *
class ScoreBoard(Turtle):
    def __init__(self,screen_width,screen_height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.x_axis = screen_height // 2
        self.y_axis = screen_width // 2
        self.level = 1
        self.goto(x = -self.x_axis + 70, y = self.y_axis - 60)
        self.write(f"Level: {self.level}", align = "center", font = ("Arial",25,"normal"))
    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align = "center", font = ("Arial",25,"normal"))
    def game_over(self):
        self.clear()
        self.goto(x = 0, y = 0)
        self.write("GAME OVER", align = "center", font = ("Arial",35,"bold"))