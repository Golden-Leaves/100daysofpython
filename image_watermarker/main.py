from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
def main():
    window = Tk()
    window.minsize(width = 900,height = 550)
    window.config(padx = 50,pady = 50,bg = "#202020")
    window.title("Image Watermarker")
    style = Style()
    style.theme_use("clam")
    style.configure("Upload_File.TButton",foreground="white",background="#196bf7",
                    relief="flat",
                    borderwidth=3,
                    padding=3
    )
    style.map("Upload_File.TButton",foreground=[("pressed", "white"),("active", "white")],
              background=[ ("pressed", "#003acc"),("active", "#338aff")]) #You need map in order to change bg color
    
    cloud_upload_img = Image.open("./images/cloud_upload_file_image.png")  #Thumbnail returns None
    cloud_upload_img.thumbnail((450, 275))
    cloud_upload_png = ImageTk.PhotoImage(cloud_upload_img) #ImageTk is a module lol, the file kw expects a file path??
    cloud_upload_width,cloud_upload_height = (cloud_upload_png.width(),cloud_upload_png.height())
    cloud_upload_image = Canvas(width=cloud_upload_width,height=cloud_upload_height,highlightthickness=0)
    canvas_image = cloud_upload_image.create_image(cloud_upload_width//2,cloud_upload_height//2,image=cloud_upload_png)
    cloud_upload_image.grid(column=0,row=0)
    
    upload_file_button = Button(text="Upload File",width=20,style="Upload_File.TButton")
    upload_file_button.grid(row=1,column=0,pady=28)
    window.grid_rowconfigure(1,weight=1)
    window.grid_columnconfigure(0,weight=1)
    window.mainloop()
if __name__ == "__main__":
    main()