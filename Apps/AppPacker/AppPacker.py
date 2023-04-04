def Main(OS):
    import os
    import PIL.ImageGrab as ImageGrab
    from PIL import ImageTk, Image
    import tkinter as T
    import json as J

    with open("Sys_Config.json","r") as C:
        Config = J.load(C)
        C.close()
    
    Res = Config["Resolution"].split("x")
    w = int(Res[0])
    h = int(Res[1])

    ProgDir = "Apps"
    ProgFolder = "AppPacker"
    icon = ImageTk.PhotoImage(Image.open(f"{ProgDir}\\{ProgFolder}\\{ProgFolder}.png"))

    Packer = T.Toplevel(OS,width=w,height=h)
    Packer.transient(OS)
    Packer.title("App Packer")
    Packer.iconphoto(False, icon)

    canvas = T.Canvas(Packer,bg="white")
    canvas.grid(row=0,column=0,sticky="nw")

    coder = T.Text(Packer, bg="light gray", width=100)
    coder.grid(row=0,column=1,rowspan=5,sticky="ns")
    coder.insert("1.0","def Main(OS): \n ProgDir = 'Apps' \n ProgFolder = 'App' #or what ever the app would be called \n icon = ImageTk.PhotoImage(Image.open(f'{ProgDir}\\{ProgFolder}\\{ProgFolder}.png'))")
    
    icon = ImageTk.PhotoImage(Image.open(f"{ProgDir}\\{ProgFolder}\\{ProgFolder}.png"))

    ProgName = T.Entry(Packer,bg="light gray")
    ProgName.grid(row=5,column=0,columnspan=1,sticky="we")
    ProgName.insert(0,"App \n")

    

    Error = T.Label(Packer,fg="red",bg="black")
    Error.grid(row=1000,columnspan=3,sticky='we')


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

    def save():
        x = Packer.winfo_rootx() + canvas.winfo_x()
        y = Packer.winfo_rooty() + canvas.winfo_y()
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        image = ImageGrab.grab(bbox=(x, y, x+width, y+height))
        image.save(f'Apps\\{ProgName.get()}.png')

        with open(f'Apps\\{ProgName.get()}',"w") as File:
            File.write(coder.get("1.0","end"))
        
        Error.insert(0,f"Saved, {ProgName.get()}!")

    #brush settings
    brush_size = 1
    global brush_color
    brush_color = (0, 0, 0)
    global color_hex
    color_hex = '#FFFFFF'
    #rgb inputs
    global red, green, blue
    red = T.Entry(Packer,bg="red")
    red.insert(0,0)
    green = T.Entry(Packer,bg="green")
    green.insert(0,0)
    blue = T.Entry(Packer,bg="blue")
    blue.insert(0,0)

    # command buttons
    color_button = T.Button(Packer, text='Change Color', command=change_color, bg=color_hex)
    saver = T.Button(Packer,text="Save",command=save)

    red.grid(row=1,column=0)
    green.grid(row=2,column=0)
    blue.grid(row=3,column=0)
    color_button.grid(row=4,column=0)
    saver.grid(row=5,column=1,sticky='we')

    

        