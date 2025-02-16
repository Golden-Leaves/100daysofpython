from tkinter import *
import time
reps = 1
work_mins = 25
short_break_mins = 5
long_break_mins = 20
timer = None
def main():
    global reps
    window = Tk()
    window.title("Pomodoro")
    window.minsize(width = 600,height = 450)
    window.config(bg = "#f7f5dd",pady = 50)
    def start_timer():
        global reps
        if reps % 8 == 0:#Long break
            status_text.config(text = "Long Break",fg = "#BF77F6")
            timer_countdown(long_break_mins*60)
        elif reps % 2 != 0:#Work
            status_text.config(text = "Work",fg = "#e7305b")
            timer_countdown(work_mins*60)
        elif reps % 2 == 0:#Short break
            marks = ""
            for mark in range(reps // 2):#"/" returns a float by defualt
                marks += "✔"
            checkmark_counter.config(text = marks)
            status_text.config(text = "Break",fg = "#BAC67A")
            timer_countdown(short_break_mins*60)
            
    def reset_timer():
        global timer
        window.after_cancel(timer)
        global reps
        reps = 1
        checkmark_counter.config(text = "")
        status_text.config(text = "Timer" ,fg  = "#FFB5C0")
        tomato_img.itemconfig(timer_text, text = "00:00")

        
    def update_date_time(new_data_time):
        current_date_time.config(text = new_data_time)
        window.after(1000,update_date_time,time.ctime())
        
    def timer_countdown(count):
        global reps
        global timer
        minutes_remaining_seconds = divmod(count,60)
        timer_minutes = minutes_remaining_seconds[0]
        timer_remaining_seconds = minutes_remaining_seconds[1]
        tomato_img.itemconfig(timer_text,text = f"{timer_minutes:02d}:{timer_remaining_seconds:02d}")
        if count > 0:
          timer = window.after(1000,timer_countdown, count - 1) 
        elif count == 0:#Starts next phase after current one ends
            reps += 1
            window.after(1000,start_timer) 



    
    tomato_png = PhotoImage(file = r"100daysofpython/tomato.png")
    tomato_img = Canvas(width = 360, height = 360,bg = "#f7f5dd", highlightthickness = 0)
    tomato_img.create_image(180,150,image = tomato_png)
    timer_text = tomato_img.create_text(180,170,text = "00:00",fill = "white", font = ("Courier",40,"bold"))
    tomato_img.grid(column = 1, row = 1)
    
    status_text = Label(text = "Timer" ,fg  = "#FFB5C0",bg = "#f7f5dd", font = ("Courier",35,"normal"))
    status_text.grid(column = 1, row = 0,sticky = "n")
    
    start_pomodoro = Button(text = "Start",command = start_timer,width = 7,relief = "flat",bg = "#FFCF96")
    start_pomodoro.grid(column = 0,row = 2,padx = 20)
    
    reset_pomodoro = Button(text = "Reset",command = reset_timer ,width = 7,relief = "flat",bg = "#FFCF96")#placeholder command
    reset_pomodoro.grid(column = 2,row = 2,padx = 20,sticky = "n")
    
    checkmark_counter = Label(text =  "", fg = "#BAC67A",font = ("Courier",15,"normal"), bg = "#f7f5dd")
    checkmark_counter.grid(column = 1, row = 3)
    
    current_date_time = Label(text = time.ctime() ,fg  = "#BAC67A",bg = "#f7f5dd", font = ("Courier",15,"bold"))
    current_date_time.grid(column = 2, row = 0,padx = 10)

    update_date_time(time.ctime())
    
    window.mainloop()
if __name__ == "__main__":
    main()