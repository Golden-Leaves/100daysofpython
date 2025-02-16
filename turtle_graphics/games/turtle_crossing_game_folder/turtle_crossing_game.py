from turtle import *
from player import *
from car_manager import *
from scoreboard import *
import time
import random
#0.1s refresh rate
def main():
    color_list = []
    while True:
      try:
        screen_width = 600
        screen_height = 600
        refresh_rate = 0.1
        break
      except ValueError:
        print("Invalid input.")
        
    screen = Screen()
    screen.setup(width = screen_width, height = screen_height)
    screen.bgcolor("black")
    screen.title("Turtle Crossing")
    screen.colormode(255)
    screen.tracer(0)
    
    for i in range(100):
      color_tuple = (random.randint(60,255),random.randint(60,255),random.randint(60,255))
      color_list.append(color_tuple)
      
    car_manager = CarManager(color_list,screen_width,screen_height)
    player = Player(screen_width,screen_height)
    scoreboard = ScoreBoard(screen_width,screen_height)
    
    screen.listen()
    screen.onkey(player.up, "w")
    
    game_is_on = True
    while game_is_on:
        screen.update()
        for car in car_manager.cars:
          if player.distance(car) < 20:
           game_is_on = False
           scoreboard.game_over()

        if player.ycor() > screen_height // 2 - 30:
          scoreboard.level_up()
          player.goto(x = player.turtle_position[0], y = player.turtle_position[1])
          car_manager.reset_cars()
          car_manager.car_speed += 5
          player.movement_distance += 1

        if random.randint(1,15) == 1 and len(car_manager.cars) < 26:
          car_manager.generate_cars()
        car_manager.move_cars()
        time.sleep(refresh_rate)
    screen.mainloop()
if __name__ == "__main__":
    main()
