from turtle import *

screen = Screen()
def move_forwards():
    global tim
    tim.forward(4)
    screen.update()
def move_backwards():
    global tim
    tim.backward(4)
    screen.update()
def turn_left():
    global tim
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    screen.update()
def turn_right():
    global tim
    next_heading = tim.heading() - 10
    tim.setheading(next_heading)
    screen.update()
def main():
    global tim
    global screen
    screen.setup(850,600)
    screen.listen()
    screen.onkeypress(key = "w",fun = move_forwards)
    screen.onkeypress(key = "s",fun = move_backwards)
    screen.onkeypress(key = "a", fun = turn_left)
    screen.onkeypress(key = "d", fun = turn_right)
    screen.mainloop()

if __name__ == "__main__":
    main()