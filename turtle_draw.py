from turtle import *
import prettytable
timmy = Turtle()
turtle_screen = Screen()
print(turtle_screen.canvheight)
timmy.shape("turtle")
timmy.color("cyan1","DarkOrange")
timmy.forward(100)
turtle_screen.exitonclick()
table = prettytable.PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)