import pandas
from turtle import *
def main():
    states = pandas.read_csv(r"100daysofpython/day-25-us-states-game-start/50_states.csv")
    blank_image = r"100daysofpython/day-25-us-states-game-start/blank_states_img.gif"
    state_names = states["state"].to_list()
    screen = Screen()
    screen.title("U.S States Game")
    screen.addshape(blank_image)
    writing_turtle = Turtle()
    writing_turtle.shape(blank_image)
    def get_mouse_coor(x,y):
        return(x,y)
    screen.onscreenclick(get_mouse_coor)
    state_coords = get_mouse_coor()
    
    screen.mainloop()
if __name__ == "__main__":
    main()