import random 
from turtle import *
# Coordinate system: y = screen_height / 2, x = screen_width / 2 ( Defualt both sides 400px, x and y both extend to 200 )

def main():

    retry_or_exit = ""
    is_race_on = False

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-70,-40,-10,20,50,80]
    screen = Screen()
    screen.setup(width = 500, height = 400)
    turtle_list = []
    for turtle_index in range(6):
        
        new_turtle = Turtle(shape = "turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtle_index])
        new_turtle.goto(x = -240, y = y_positions[turtle_index])
        turtle_list.append(new_turtle)
    try:
      user_bet = screen.textinput(title = "Make your bet", prompt= "Which turtle will win the race?: ").lower()
    except AttributeError:#Occurs when the player doesnt type anything.
        return
    if user_bet:
        is_race_on = True
    while is_race_on:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                is_race_on = False
                turtle_color = turtle.pencolor()
                if turtle_color == user_bet:
                    screen.textinput(title= f"You've won, the winning color is {turtle_color}!", prompt = "Type anything to continue...")
                else:
                    screen.textinput(title= f"You've lost, the winning color is {turtle_color}!", prompt = "Type anything to continue...")
                    
                retry_or_exit = screen.textinput(title = "Play again?",prompt="Type 'exit' to exit the game, 'retry' to restart")
                
                
            turtle.forward(random.randint(0,10))
        if retry_or_exit == "retry":
            screen.clear()
            main()
        elif retry_or_exit == "exit":
            screen.bye()
            return
        
    screen.exitonclick()
if __name__ == "__main__":
    main()