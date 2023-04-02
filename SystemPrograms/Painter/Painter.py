def Main(OS):
    import tkinter as T
    from PIL import Image, ImageTk
    import os

    easel = T.Toplevel(OS)
    easel.transient(OS)

    #loads the image to a canvas
    H = 400
    W = 400

    global canvas
    canvas = T.Canvas(easel, bg="white", width=W, height=H)
    canvas.pack()

    #brush settings
    brush_size = 1
    brush_color = (0, 0, 0)

    global color_hex
    color_hex = '#FFFFFF'
    
    Location = "paint"

    #rgb inputs
    global red, green, blue
    red = T.Entry(easel,bg="red")
    red.insert(0,0)
    green = T.Entry(easel,bg="green")
    green.insert(0,0)
    blue = T.Entry(easel,bg="blue")
    blue.insert(0,0)

    name = T.Entry(easel)

    def save_canvas():
        global canvas
        filename = name.get()
        if filename:
            canvas.postscript(file=os.path.join(Location, filename + ".eps"))
            img = ImageTk.PhotoImage(Image.open(os.path.join(Location, filename + ".eps")))
            img.save(os.path.join(Location, filename + "png"), "PNG")
            os.remove(os.path.join(Location, filename + ".eps"))

    #functions
    def change_color():
        global red, green, blue, brush_color
        r_val = int(red.get())
        g_val = int(green.get())
        b_val = int(blue.get())
        brush_color = (r_val, g_val, b_val)


    def paint(event):
        x, y = event.x, event.y
        red, green, blue = brush_color
        global color_hex
        color_hex = f'#{red:02x}{green:02x}{blue:02x}'  #RGB to Hex
        canvas.create_rectangle(x, y, x+brush_size, y+brush_size, fill=color_hex, outline=color_hex)

    canvas.bind('<B1-Motion>', paint)

    # color button
    color_button = T.Button(easel, text='Change Color', command=change_color, bg=color_hex)
    save_button = T.Button(easel, text='Save', command=save_canvas, bg="blue")

    red.pack()
    green.pack()
    blue.pack()
    color_button.pack()
    name.pack()
    save_button.pack()

    easel.mainloop()

def redraw(OS,select,Location):
    import tkinter as T
    from PIL import Image, ImageTk
    import math
    import os

    easel = T.Toplevel(OS)

    #loads the image to a canvas
    H = 400 
    W = 400
    image = Image.open(f"{Location}\\{select}")
    if (image.width,image.height) < (W,H):
        dW = math.trunc(W/image.width)
        dH = math.trunc(H/image.height)
        image = image.resize((image.width*dW,image.height*dH))
    photo = ImageTk.PhotoImage(image)
    canvas = T.Canvas(easel, bg="white", width=image.width, height=image.height)
    canvas.create_image(0, 0, anchor=T.NW, image=photo)
    canvas.pack()

    #brush settings
    brush_size = math.trunc(dH/dW)
    brush_color = (0, 0, 0)

    global color_hex
    color_hex = '#FFFFFF'

    #rgb inputs
    global red, green, blue
    red = T.Entry(easel,bg="red")
    green = T.Entry(easel,bg="green")
    blue = T.Entry(easel,bg="blue")

    name = T.Entry(easel)

    def save_canvas():
        filename = name.get()
        if filename:
            canvas.postscript(file=os.path.join(Location, filename + ".eps"))
            img = Image.open(Location + filename + ".eps")
            img.save(os.path.join(Location, filename + "png"), "PNG")
            os.remove(os.path.join(Location, filename + "eps"))

    #functions
    def change_color():
        global red, green, blue, brush_color
        r_val = int(red.get())
        g_val = int(green.get())
        b_val = int(blue.get())
        brush_color = (r_val, g_val, b_val)


    def paint(event):
        x, y = event.x, event.y
        red, green, blue = brush_color
        global color_hex
        color_hex = f'#{red:02x}{green:02x}{blue:02x}'  #RGB to Hex
        canvas.create_rectangle(x, y, x+brush_size, y+brush_size, fill=color_hex, outline=color_hex)

    canvas.bind('<B1-Motion>', paint)

    # color button
    color_button = T.Button(easel, text='Change Color', command=change_color, bg=color_hex)
    save_button = T.Button(easel, text='Save', command=save_canvas, bg="blue")

    red.pack()
    green.pack()
    blue.pack()
    color_button.pack()
    name.pack()
    save_button.pack()

    easel.mainloop()