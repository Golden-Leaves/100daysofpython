from turtle import *
import random
import time
from snake_class import *
from food import *
from scoreboard import *
def main():
    while True:
      try:
        screen_width = 600
        screen_height = 600
        break
      except ValueError:
        print("Invalid input.")
    game_is_on = True
    screen = Screen()
    screen.setup(width = screen_width, height = screen_height)
    screen.bgcolor("black")
    
    
    screen.title("Snake Game")
    screen.tracer(0) #No animation
    
    snake = Snake()
    food = Food(screen_width,screen_height)
    scoreboard = ScoreBoard(screen_height)
    
    print("Prepare to start!")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Game start.")
    
    screen.update()
    screen.listen()
    screen.onkey(snake.up,"w")
    screen.onkey(snake.left,"a")
    screen.onkey(snake.down,"s")
    screen.onkey(snake.right,"d")
    while game_is_on:
      screen.update()
      time.sleep(0.1)
      snake.move()
      #Food collision
      if snake.segments[0].distance(food) < 15:
        scoreboard.score += 1
        scoreboard.update_score()
        food.refresh()
        snake.extend(snake.segments[-1].position())
        screen.update()
      #Wall collision:
      if snake.segments[0].xcor() > screen_width // 2 or snake.segments[0].xcor() < (screen_width // 2) * -1 or snake.segments[0].ycor() > screen_height // 2 or snake.segments[0].ycor() < (screen_height //2) * -1:
        scoreboard.reset()
        snake.reset()


      #Body collision:
      for segment in snake.segments[1:]:
          if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    retry = input("Type 'retry' to retry, type anything else to quit: ").lower()
    if retry == "retry":
      game_is_on = True
      main()
    else:
      return

  
    screen.mainloop()
    
if __name__ == "__main__":
    main()