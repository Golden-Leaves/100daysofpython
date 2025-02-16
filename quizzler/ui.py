from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

        
    def __init__(self,quiz:QuizBrain) -> None:
        self.quiz = quiz
 

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg = THEME_COLOR,padx = 20,pady = 20)
        self.window.minsize(width = 280,height = 520)
        
        self.score_text = Label(text = f"Score: {self.quiz.score} ",bg = THEME_COLOR,fg = "#FFFFFF")
        self.score_text.grid(column = 1,row = 0,pady  = 20,sticky = "n")
        

        self.canvas = Canvas(height = 250, width = 300,highlightthickness = 0)
        self.canvas_text = self.canvas.create_text(125,150,font = ("Arial",20,"italic"),text = "",width = 250)
        self.canvas.grid(row = 1,column = 0,columnspan = 2)
        
        
        self.false = PhotoImage(file =  "100daysofpython/quizzler/images/false.png")
        self.false_button = Button(image = self.false,highlightthickness = 0,relief = 'flat',command = self.false_pressed)
        self.false_button.grid(row = 2,column =  1,padx = 20,pady = 60)
        
        self.true = PhotoImage(file = "100daysofpython/quizzler/images/true.png")
        self.true_button = Button(image = self.true,relief = "flat", highlightthickness = 0,command = self.true_pressed)
        self.true_button.grid(column = 0,row = 2,padx = 20,pady = 60)
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg = "#FFFFFF")
        if self.quiz.still_has_questions():      
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text = question_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text = "You've reached the end of the quiz!")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")
            
            
    def false_pressed(self):
            is_right =  self.quiz.check_answer("False")
            self.score_text.config(text = f"Score: {self.quiz.score}")
            self.give_feedback(is_right)
        
    def true_pressed(self):
            is_right = self.quiz.check_answer("True")
            self.score_text.config(text = f"Score: {self.quiz.score}")
            self.give_feedback(is_right)
            
    def give_feedback(self,outcome):
        if outcome == True:
            self.canvas.config(bg = "#00FF00")
        else:
            self.canvas.config(bg = "#FF0000")
        self.window.after(1000,self.get_next_question)
    
        
       
