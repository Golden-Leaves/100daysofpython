from turtle import *
from paddle import *
from ball import *
from scoreboard import *
import time
# LENGTH IS THE WIDTH

def main():

    while True:
      try:
        screen_width = 800
        screen_height = 600
        ball_speed = int(input("For more customizability, input the ball's speed (recommended is 5): "))
        paddle_speed = int(input("Input the paddle's speed (recommended is 25): "))
        break
      except ValueError:
        print("Invalid input.")  
        
    l_paddle = (screen_width) // 2 * -1 + 20 # pos
    r_paddle = screen_width // 2 -25 # pos
        
    screen = Screen()
    screen.tracer(0)
    screen.bgcolor("black")
    screen.setup(width = screen_width, height = screen_height)
    screen.title("Pong")
    
    left_paddle = Paddle(screen_width,l_paddle,paddle_speed)
    right_paddle = Paddle(screen_width,r_paddle,paddle_speed)
    ball = Ball(screen_width,screen_height,ball_speed)
    score_board = Scoreboard(screen_height)
    #Countdown
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
#TODO make big text that flash up on screen with the scoreboard module next
    
    screen.update()
    screen.listen()
    screen.onkey(left_paddle.go_up,"w")
    screen.onkey(left_paddle.go_down,"s")
    screen.onkey(right_paddle.go_up, "Up")
    screen.onkey(right_paddle.go_down, "Down")
    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()
        time.sleep(ball.sleep_value)
        
        #Border collision
        if ball.ycor() > screen_height // 2 - 20 or ball.ycor() < (screen_height // 2) * -1 + 20 :
          ball.bounce_y()
        #Paddle collision
        if (ball.xcor() > screen_width // 2 -40 and ball.distance(right_paddle) < 50) or (ball.xcor() < (screen_width) // 2 * -1 + 30 and ball.distance(left_paddle) < 50) :# -40 because the distacne to center of the paddle is 20 (.goto() only takes into account the cetner of the object)
          ball.bounce_x() 

          

        if ball.xcor() > screen_width // 2 -20 :
          ball.reset_position()
          score_board.r_score += 1
          score_board.r_score_increase()
          
        elif ball.xcor() < (screen_width) // 2 * -1 + 15:
          ball.reset_position()
          score_board.l_score += 1
          score_board.l_score_increase()

        


  


    
    screen.mainloop()
if __name__ == "__main__":
    main()