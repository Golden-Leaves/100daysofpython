from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import filedialog

def main():
    window_width = 1400
    window_height = 650
    master = Tk()
    master.minsize(width=window_width, height=window_height)
    master.config(bg="#303030")
    master.title("Image Watermarker")

    def open_file():
        #Opens File Explorer
        filename = filedialog.askopenfilename(initialdir="r", title="Open an Image",
                                              filetypes=(("Image Files", "*.jpg *.jpeg *.png *.webp"), ("All Files", "*.*")))
        if filename:
            user_img_PIL = Image.open(filename)
            canvas_width = window_width
            canvas_height = window_height - 125
            user_img_PIL.thumbnail((canvas_width, canvas_height))
            user_img = ImageTk.PhotoImage(user_img_PIL) #ImageTk is a module lol, the file kw expects a file path??
            image_canvas.configure(width=canvas_width, height=canvas_height)
            image_canvas.itemconfig(canvas_image, image=user_img)
            image_canvas.coords(canvas_image, canvas_width // 2, canvas_height // 2)
            #Keeps reference to the image otherwise it gets garbage collected
            image_canvas.im = user_img #https://stackoverflow.com/questions/57049722/unable-to-update-image-in-tkinter-using-a-function
            upload_file_button.destroy()
            button_frame.grid(row=1, column=0, pady=10)
            return user_img
        else:
            print("No file selected.")
    
    def add_logo():
        pass
    def add_text():
        pass

    style = Style()
    style.theme_use("clam")
    style.configure("Upload_File.TButton", foreground="white", background="#196bf7",
                    relief="flat", borderwidth=0, padding=3,font=("Helvetica",9))
    style.configure("Add.TButton", foreground="white", background="#303030",
                     relief = "flat", padding=3,font=("Helvetica",10),
                      darkcolor="white",
                      lightcolor="gray",
                     bordercolor="white")
    style.configure("TFrame",  background="#303030",
                    relief="flat", borderwidth=0, padding=3)
    style.map("Upload_File.TButton",
              foreground=[("pressed", "white"), ("active", "white")],
              background=[("pressed", "#003acc"), ("active", "#338aff")])
    style.map("Add.TButton",
              foreground=[("pressed", "white"), ("active", "white")],
              background=[("pressed", "#202020"), ("active", "#404040")])

    cloud_upload_img = Image.open("./images/cloud_upload_image.png")
    cloud_upload_width, cloud_upload_height = cloud_upload_img.size
    cloud_upload_img.thumbnail((cloud_upload_width - 200, cloud_upload_height - 100))
    cloud_upload_png = ImageTk.PhotoImage(cloud_upload_img)

    canvas_width = window_width - 500
    canvas_height = window_height - 425
    image_canvas = Canvas(master, width=canvas_width, height=canvas_height, highlightthickness=0,
                          bg=master["bg"])
    canvas_image = image_canvas.create_image(
        canvas_width // 2,
        canvas_height // 2,
        image=cloud_upload_png,
        anchor="center"
    )
    image_canvas.grid(column=0, row=0)

    upload_file_button = Button(master, text="Upload File", padding=(20, 8),
                                style="Upload_File.TButton", command=open_file)
    upload_file_button.grid(row=1, column=0, pady=10)

    button_frame = Frame(master, style="TFrame", padding=10)
    # Don't grid it until after upload
    add_text_button = Button(button_frame, text="Add Text", padding=(20, 8),
                             style="Upload_File.TButton", command=add_text)
    add_logo_button = Button(button_frame, text="Add Logo", padding=(20, 8),
                             style="Upload_File.TButton", command=add_logo)
    add_text_button.pack(side=LEFT, padx=10)
    add_logo_button.pack(side=LEFT, padx=10) #Packs them side-by-side in the frame

    master.grid_rowconfigure(0, weight=1)
    master.grid_rowconfigure(1, weight=1)
    master.grid_columnconfigure(0, weight=1)
    master.mainloop()

if __name__ == "__main__":
    main()
