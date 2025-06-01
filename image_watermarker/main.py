from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
from tkinter import filedialog

def main():
    window_width = 1400
    window_height = 650
    window = Tk()
    window.minsize(width = window_width,height = window_height)
    window.config(bg = "#202020")
    window.title("Image Watermarker")
    def open_file():
        #Opens file explorer
        filename = filedialog.askopenfilename(initialdir="r",title="Open an Image",
                                          filetypes=(("Image Files","*.jpg *.jpeg *.png *.webp"),("All Files", "*.*")))#Dropdown menu to select file types
         
        if filename:  #Checks if the user selected a file
            
            user_img_PIL = Image.open(filename)
            canvas_width = window_width
            canvas_height = window_height - 125
            user_img_PIL.thumbnail((canvas_width, canvas_height))
            user_img =  ImageTk.PhotoImage(user_img_PIL)
            image_canvas.configure(width=canvas_width, height=canvas_height)
            image_canvas.itemconfig(canvas_image,image=user_img)
            image_canvas.coords(canvas_image,canvas_width//2,canvas_height//2) #Update coords since canvas size changed lol
            #Keeps reference to the image otherwise it gets garbage collected
            image_canvas.im = user_img #https://stackoverflow.com/questions/57049722/unable-to-update-image-in-tkinter-using-a-function
            return user_img 
        else:
            print("No file selected.")
            
    style = Style()
    style.theme_use("clam")
    style.configure("Upload_File.TButton",foreground="white",background="#196bf7",
                    relief="flat",
                    borderwidth=0,
                    padding=3,
                    
    )
    style.map("Upload_File.TButton",foreground=[("pressed", "white"),("active", "white")],
              background=[ ("pressed", "#003acc"),("active", "#338aff")]) #You need map in order to change bg color
    
    cloud_upload_img = Image.open("./images/cloud_upload_image.png")  #Thumbnail returns None
    cloud_upload_width,cloud_upload_height = cloud_upload_img.size
    cloud_upload_img.thumbnail((cloud_upload_width - 200 , cloud_upload_height - 100 ))
    cloud_upload_png = ImageTk.PhotoImage(cloud_upload_img) #ImageTk is a module lol, the file kw expects a file path??
    
    canvas_width = window_width - 500
    canvas_height = window_height - 425
    image_canvas = Canvas(width=canvas_width, height=canvas_height, highlightthickness=0,
                          bg=window["bg"])  # Makes the bg transparent by setting it the same color as the window
    
    canvas_image = image_canvas.create_image(
        canvas_width // 2,
        canvas_height // 2,
        image=cloud_upload_png,
        anchor="center",
    )
    image_canvas.grid(column=0, row=0)
    
    upload_file_button = Button(text="Upload File", padding=(20, 8), style="Upload_File.TButton", command=open_file)
    upload_file_button.grid(row=1, column=0, pady=10)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.mainloop()

if __name__ == "__main__":
    main()
