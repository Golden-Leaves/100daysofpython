from turtle import *
import random
import time
from snake_class import *
def main():
    game_is_on = True
    screen = Screen()
    snake = Snake()
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0) #No animation
    screen.update()
    while game_is_on:
      screen.update()
      time.sleep(0.1)
      snake.move()

  
    screen.exitonclick()
    
if __name__ == "__main__":
    main()