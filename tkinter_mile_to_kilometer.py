from tkinter import *
def main():
    window = Tk()
    window.title("Kilometers to miles converter")
    window.minsize(width = 300, height = 150)
    window_text = Label(text = "is equal to", font = ("Arial",13,"italic"), master = window)
    window_text.grid(row = 1, column = 0, padx = 10,pady = 10)
 
    def calculate_miles():
        try:
            kilometers = int(kilometers_input.get())
            miles = round(kilometers *  0.621371, ndigits = 2)
            miles_result.config(text = miles)

        except ValueError:
           kilometers_input.delete(first = 0, last = END)
           kilometers_input.insert(END, string = "Invalid.")
        

  
       
    button = Button(text = "Convert", command = calculate_miles, master = window)
    button.grid(column  = 1, row = 2)
    
    
    kilometers_input = Entry(width = 10, master = window)
    kilometers_input.insert(END, string = "0")
    kilometers_input.grid(column =  1, row = 0)
    
    kilometers_label = Label(text = "Kilometers", font = ("Arial",13,"normal"), master = window )
    kilometers_label.grid(column = 2, row = 0,padx = 10)
    
    miles_result = Label(text = "0", font = ("Arial",13,"normal"), master = window)
    miles_result.grid(column = 1, row = 1)
    miles_label = Label(text = "Miles", font = ("Arial",13,"normal"), master = window )
    miles_label.grid(column = 2, row = 1,padx = 10)
    
    
        
    window.mainloop()
if __name__ == "__main__":
    main()    