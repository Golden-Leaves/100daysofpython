from turtle import *
import pandas
#TODO: THE GODDAMN IMAGE WONT FIT THE ENTIRE WINDOW FOR SOME REASON
def main():
    us_states_data = pandas.read_csv(r"100daysofpython/day-25-us-states-game-start/50_states.csv")
    blank_image = r"100daysofpython/day-25-us-states-game-start/blank_states_img.gif"
    state_names = us_states_data["state"].to_list()
    screen = Screen()
    screen.title("U.S States Game")
    screen.addshape(blank_image)
    #image_turtle = Turtle()
    #image_turtle.shape(blank_image)
    #image_turtle.penup()
    screen.bgpic(blank_image)
    def get_mouse_coor(x,y):
        print(x,y)
    screen.onscreenclick(get_mouse_coor)
    guessed_states = []

    while len(guessed_states) <= 50:
        #Hi, the word to exit the game is "Exit" (case-sensitive)
      state_answer = screen.textinput(title = "Guess the state.", prompt = "Enter a state's name.")
      state_answer = state_answer.title()
      if state_answer == "Exit":
          break
      if state_answer in state_names and state_answer not in guessed_states:
          guessed_states.append(state_answer)
          writing_turtle = Turtle()
          writing_turtle.penup()
          writing_turtle.hideturtle()
          state_answer_row = us_states_data[us_states_data["state"] == state_answer]
          state_answer_x = state_answer_row["x"].item() #By defualt returns Series ({Index}, {Actual data}), so need to ca;; .item() to get the data
          state_answer_y = state_answer_row["y"].item()
          print(state_answer_x,state_answer_y)
          writing_turtle.goto(x = state_answer_x, y = state_answer_y)
          writing_turtle.write(state_answer, align = "center", font = ("Arial",10,"normal"))
    
 
if __name__ == "__main__":
    main()