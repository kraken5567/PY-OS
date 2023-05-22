import tkinter as T
from PIL import Image, ImageTk
import math
import PIL.ImageGrab as ImageGrab
import SystemPrograms.FileFinder.FileFinder as FF

def Main(OS):
    
    easel = T.Toplevel(OS)
    easel.transient(OS)
    easel.title("Paint")

    def create_canvas():
        nonlocal canvas, display_width, display_height, image_width, image_height

        display_width = int(display_width_entry.get())
        display_height = int(display_height_entry.get())
        image_width = int(image_width_entry.get())
        image_height = int(image_height_entry.get())

        canvas.destroy()  # Destroy the existing canvas

        canvas = T.Canvas(easel, bg="white", width=display_width, height=display_height)
        canvas.grid(row=4, column=0, columnspan=2)

        brush_size = min(display_width // image_width, display_height // image_height)
        canvas.bind('<B1-Motion>', lambda event: paint(event, display_width, display_height, image_width, image_height, brush_size))

    def paint(event, display_width, display_height, image_width, image_height, brush_size):
        x, y = event.x, event.y
        row = x // (display_width // image_width)
        col = y // (display_height // image_height)
        x1 = row * brush_size
        y1 = col * brush_size
        x2 = x1 + brush_size
        y2 = y1 + brush_size
        red, green, blue = brush_color
        color_hex = f'#{red:02x}{green:02x}{blue:02x}'  # RGB to Hex
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_hex, outline=color_hex)

    # Prompt for display resolution
    display_prompt = T.Label(easel, text="Enter the display resolution:")
    display_prompt.grid(row=0, column=0, columnspan=2)

    display_width_entry = T.Entry(easel)
    display_width_entry.grid(row=1, column=0)

    display_height_entry = T.Entry(easel)
    display_height_entry.grid(row=1, column=1)

    # Prompt for image resolution
    image_prompt = T.Label(easel, text="Enter the image resolution:")
    image_prompt.grid(row=2, column=0, columnspan=2)

    image_width_entry = T.Entry(easel)
    image_width_entry.grid(row=3, column=0)

    image_height_entry = T.Entry(easel)
    image_height_entry.grid(row=3, column=1)

    # Apply button
    apply_button = T.Button(easel, text="Apply", command=create_canvas)
    apply_button.grid(row=4, column=2, sticky="ns")

    # Initialize canvas
    display_width = 256
    display_height = 256
    image_width = 32
    image_height = 32

    #insert values
    display_height_entry.insert(0,f"{display_height}")
    display_width_entry.insert(0,f"{display_width}")
    image_height_entry.insert(0,f"{image_height}")
    image_width_entry.insert(0,f"{image_width}")

    canvas = T.Canvas(easel, bg="white", width=display_width, height=display_height)
    canvas.grid(row=5, column=0, columnspan=2)

    # Brush settings
    global brush_color
    brush_size = (display_height/display_width)//(image_height/image_width)
    brush_color = (0, 0, 0)

    def change_settings(a):
        global brush_color
        if a:
            r_val = int(red.get())
            g_val = int(green.get())
            b_val = int(blue.get())
            color_E_button.configure(bg=f'#{r_val:02x}{g_val:02x}{b_val:02x}')
        else:
            r_val = int(redSlider.get())
            g_val = int(greenSlider.get())
            b_val = int(blueSlider.get())
            color_S_button.configure(bg=f'#{r_val:02x}{g_val:02x}{b_val:02x}')
        brush_color = (r_val, g_val, b_val)

    # RGB inputs
    red = T.Entry(easel, bg="red")
    red.insert(0, 0)
    red.grid(row=6, column=0)

    green = T.Entry(easel, bg="green")
    green.insert(0, 0)
    green.grid(row=7, column=0)

    blue = T.Entry(easel, bg="blue")
    blue.insert(0, 0)
    blue.grid(row=8, column=0)

    redSlider = T.Scale(easel, bg="red", from_=0, to=255, orient=T.HORIZONTAL)
    redSlider.grid(row=6, column=1)

    greenSlider = T.Scale(easel, bg="green", from_=0, to=255, orient=T.HORIZONTAL)
    greenSlider.grid(row=7, column=1)

    blueSlider = T.Scale(easel, bg="blue", from_=0, to=255, orient=T.HORIZONTAL)
    blueSlider.grid(row=8, column=1)

    color_E_button = T.Button(easel, text='Change Color (Entry)', command=lambda: change_settings(True))
    color_E_button.grid(row=9, column=0, sticky='we')

    color_S_button = T.Button(easel, text='Change Color (Sliders)', command=lambda: change_settings(False))
    color_S_button.grid(row=9, column=1, sticky='we')

    def save_canvas():
        x = easel.winfo_rootx() + canvas.winfo_x()
        y = easel.winfo_rooty() + canvas.winfo_y()
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        image = ImageGrab.grab(bbox=(x, y, x + width, y + height))

        Location = FF.FFImported(OS)
        if "." in Location[-4:]:
            image.save(f'{Location}')
        elif "." not in Location[-4:]:
            image.save(f'{Location}\\{name.get()}.png')

    name = T.Entry(easel)
    name.grid(row=10, column=0)

    saver = T.Button(easel, text="Save", command=save_canvas)
    saver.grid(row=10, column=1, sticky='we')

    easel.mainloop()

def redraw(OS,select,Location):

    easel = T.Toplevel(OS)
    easel.transient(OS)
    easel.title("Paint")
    ProgDir = "SystemPrograms"
    ProgFolder = "Painter"
    icon = ImageTk.PhotoImage(Image.open(f"{ProgDir}\\{ProgFolder}\\{ProgFolder}.png"))
    easel.iconphoto(False, icon)

    # Initialize canvas
    image_width = 256
    image_height = 256

    # Load and resize the image
    image = Image.open(f"{Location}\\{select}")
    image = image.resize((image_width, image_height))
    photo = ImageTk.PhotoImage(image)

    canvas = T.Canvas(easel, width=image_width, height=image_height)
    canvas.create_image(0, 0, anchor=T.NW, image=photo)

    def create_canvas():
        nonlocal image_width, image_height
        image = Image.open(f"{Location}\\{select}")
        photo = ImageTk.PhotoImage(image)
        canvas.configure(width=image_width, height=image_height)
        canvas.create_image(0, 0, anchor=T.NW, image=photo)
    
    def paint(event, image_width, image_height, brush_size):
        x, y = event.x, event.y
        scale_x = image_width / canvas.winfo_width()
        scale_y = image_height / canvas.winfo_height()
        x1 = (x - brush_size / 2) * scale_x
        y1 = (y - brush_size / 2) * scale_y
        x2 = (x + brush_size / 2) * scale_x
        y2 = (y + brush_size / 2) * scale_y
        red, green, blue = brush_color
        color_hex = f'#{red:02x}{green:02x}{blue:02x}'  # RGB to Hex
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_hex, outline=color_hex)

    canvas.bind('<B1-Motion>', lambda event: paint(event, image.width, image.height, brush_size))

    # Prompt for image resolution
    image_prompt = T.Label(easel, text="Enter the image resolution:")
    image_prompt.grid(row=2, column=0, columnspan=2)

    image_width_entry = T.Entry(easel)
    image_width_entry.grid(row=3, column=0)

    image_height_entry = T.Entry(easel)
    image_height_entry.grid(row=3, column=1)

    # Apply button
    apply_button = T.Button(easel, text="Apply", command=create_canvas)
    apply_button.grid(row=4, column=2, sticky="ns")

    #insert values
    image_height_entry.insert(0,f"{image_height}")
    image_width_entry.insert(0,f"{image_width}")

    canvas.grid(row=5, column=0, columnspan=2)

    # Brush settings
    global brush_color
    brush_size = (image_height//image.height) // (image_width//image.width)
    brush_color = (0, 0, 0)

    def change_settings(a):
        global brush_color
        if a:
            r_val = int(red.get())
            g_val = int(green.get())
            b_val = int(blue.get())
            color_E_button.configure(bg=f'#{r_val:02x}{g_val:02x}{b_val:02x}')
        else:
            r_val = int(redSlider.get())
            g_val = int(greenSlider.get())
            b_val = int(blueSlider.get())
            color_S_button.configure(bg=f'#{r_val:02x}{g_val:02x}{b_val:02x}')
        brush_color = (r_val, g_val, b_val)

    # RGB inputs
    red = T.Entry(easel, bg="red")
    red.insert(0, 0)
    red.grid(row=6, column=0)

    green = T.Entry(easel, bg="green")
    green.insert(0, 0)
    green.grid(row=7, column=0)

    blue = T.Entry(easel, bg="blue")
    blue.insert(0, 0)
    blue.grid(row=8, column=0)

    redSlider = T.Scale(easel, bg="red", from_=0, to=255, orient=T.HORIZONTAL)
    redSlider.grid(row=6, column=1)

    greenSlider = T.Scale(easel, bg="green", from_=0, to=255, orient=T.HORIZONTAL)
    greenSlider.grid(row=7, column=1)

    blueSlider = T.Scale(easel, bg="blue", from_=0, to=255, orient=T.HORIZONTAL)
    blueSlider.grid(row=8, column=1)

    color_E_button = T.Button(easel, text='Change Color (Entry)', command=lambda: change_settings(True))
    color_E_button.grid(row=9, column=0, sticky='we')

    color_S_button = T.Button(easel, text='Change Color (Sliders)', command=lambda: change_settings(False))
    color_S_button.grid(row=9, column=1, sticky='we')

    def save_canvas():
        x = easel.winfo_rootx() + canvas.winfo_x()
        y = easel.winfo_rooty() + canvas.winfo_y()
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        image = ImageGrab.grab(bbox=(x, y, x + width, y + height))

        Location = FF.FFImported(OS)
        if "." in Location[-4:]:
            image.save(f'{Location}')
        elif "." not in Location[-4:]:
            image.save(f'{Location}\\{name.get()}.png')

    name = T.Entry(easel)
    name.grid(row=10, column=0)

    saver = T.Button(easel, text="Save", command=save_canvas)
    saver.grid(row=10, column=1, sticky='we')

    easel.mainloop()
