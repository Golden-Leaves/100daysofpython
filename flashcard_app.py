from tkinter import *
import random
import pandas
import os
current_card = {}
flip_timer = None
def main():   
    if not os.path.exists(r"100daysofpython/words_to_learn.csv"):
        words = pandas.read_csv(r"100daysofpython/french_words.csv")
    else:
        words = pandas.read_csv(r"100daysofpython/words_to_learn.csv")
        
    words_dictionairy = words.to_dict(orient = "records")
    
    window = Tk()
    window.minsize(width = 900,height = 550)
    window.config(padx = 50,pady = 50,bg = "#b1ddc6")
    window.title("Flashcard App")
    
    


 

    def get_next_card():
        global current_card,flip_timer
        if not flip_timer == None:
          window.after_cancel(flip_timer)
        current_card["French"] = random.choice(words_dictionairy)["French"]
        current_card["English"] = random.choice(words_dictionairy)["English"]
        print(current_card)
        card_image.itemconfig(word_text,text = current_card["French"],fill = "#000000")
        card_image.itemconfig(text_static,text = "French",fill = "#000000")
        card_image.itemconfig(canvas_image, image = card_front_png)
        flip_timer = window.after(3000,flip_card)
 
        
    def flip_card():
        english_word = current_card["English"]
        card_image.itemconfig(text_static,text = 'English', fill = "#FFFFFF")
        card_image.itemconfig(word_text,text = english_word, fill = "#FFFFFF")
        card_image.itemconfig(canvas_image,image = card_back_png )
    
    def is_known():
        global current_card
        try:
            words_dictionairy.remove(current_card)
            get_next_card()
        except ValueError:
            get_next_card()

            
    card_front_png = PhotoImage(file = r"100daysofpython/card_front.png")
    card_back_png = PhotoImage(file = r"100daysofpython/card_back.png")
    card_image = Canvas(width = 800,height = 526,highlightthickness = 0)
    canvas_image = card_image.create_image(400,263,image  = card_front_png)
    
    word_text = card_image.create_text(400,263,text = "",font = ("Arial",60,"bold"),fill = "#000000")
    text_static = card_image.create_text(400,150,text = "",font = ("Arial",40,"italic"),fill = "#000000")
    card_image.grid(columnspan = 2,column = 0,row = 0)
    
    checkmark_png = PhotoImage(file = r"100daysofpython/right.png")
    checkmark_button = Button(image = checkmark_png, highlightthickness = 0,relief = "flat",command = is_known)
    checkmark_button.grid(column = 1,row = 1,padx = 20,pady = 20)
    
    cross_png = PhotoImage(file = r"100daysofpython/wrong.png")
    cross_button = Button(image = cross_png,highlightthickness = 0,relief = "flat")
    cross_button.grid(column = 0,row = 1,padx = 20,pady = 20)

    
    
    
    window.mainloop()
if __name__ == "__main__":
    main()

                
        
        
  