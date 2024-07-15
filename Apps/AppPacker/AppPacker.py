def Main(OS):
    import PIL.ImageGrab as ImageGrab
    from PIL import ImageTk, Image
    import tkinter as T
    import json as J
    import os

    from WindowsClass import MovableFrame as MF

    with open("Sys_Config.json","r") as C:
        Config = J.load(C)
        C.close()
    
    Res = Config["Resolution"].split("x")
    w = int(int(Res[0])//2)
    h = int(int(Res[1])//2)

    d = T.IntVar(value=256)
    imageres = T.IntVar(value=32)
    brush_size = d.get()//imageres.get()

    color_hex = T.StringVar(value='#FFFFFF')
    message = T.StringVar()

    ProgDir = "Apps"
    ProgFolder = "AppPacker"

    Frame = MF(OS,Image.open(f"{ProgDir}\\{ProgFolder}\\{ProgFolder}.png"),[w,h])
    Packer = Frame.frame

    canvas = T.Canvas(Packer,bg="white", height=d.get(), width=d.get())

    coder = T.Text(Packer, bg="light gray", width=64)
    
    coder.insert("1.0","def Main(OS): \n import tkinter as T \n from WindowsClass import MovableFrame as MF \n from PIL import Image \n width = 300; height = width; \n ProgDir = 'Apps' \n ProgFolder = #put app name here \n App = MF(OS,Image.open(f'{ProgDir}\\{ProgFolder}\\{ProgFolder}.png'),[width, height] ) \n App = App.frame \n App.mainloop()" )

    ProgName = T.Entry(Packer,bg="light gray")
    
    ProgName.insert(0,"App")

    Error = T.Label(Packer,fg="red",bg="black",textvariable=message)

    #brush settings
    global brush_color
    brush_color = (0, 0, 0) 
    red = T.Entry(Packer,bg="red")
    red.insert(0,0)
    green = T.Entry(Packer,bg="green")
    green.insert(0,0)
    blue = T.Entry(Packer,bg="blue")
    blue.insert(0,0)

    redSlider = T.Scale(Packer,bg="red",from_=0, to=255, orient=T.HORIZONTAL)
    greenSlider = T.Scale(Packer,bg="green",from_=0, to=255, orient=T.HORIZONTAL)
    blueSlider = T.Scale(Packer,bg="blue",from_=0, to=255, orient=T.HORIZONTAL)

    def change_settings(a):
        global brush_color
        if a:
            r_val = int(red.get())
            g_val = int(green.get())
            b_val = int(blue.get())
            color_E_button.configure(bg = f'#{r_val:02x}{g_val:02x}{b_val:02x}')
        else:
            r_val = int(redSlider.get())
            g_val = int(greenSlider.get())
            b_val = int(blueSlider.get())
            color_S_button.configure(bg = f'#{r_val:02x}{g_val:02x}{b_val:02x}')
        brush_color = (r_val, g_val, b_val)

    def paint(event):
        x, y = event.x, event.y
        row, col = x // brush_size, y // brush_size
        x1 = row * brush_size
        y1 = col * brush_size
        x2 = x1 + brush_size
        y2 = y1 + brush_size
        red, green, blue = brush_color
        color_hex = f'#{red:02x}{green:02x}{blue:02x}'  # RGB to Hex
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_hex, outline=color_hex)

    
    canvas.bind('<B1-Motion>', lambda event: paint(event))

    def save():
        x = Packer.winfo_rootx() + canvas.winfo_x()
        y = Packer.winfo_rooty() + canvas.winfo_y()
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        
        appdir = os.path.join("Apps\\",ProgName.get())
        appdir = os.path.join(os.getcwd(),appdir)
        os.mkdir(appdir)

        image = ImageGrab.grab(bbox=(x, y, x+width, y+height))
        image.save(f'Apps\\{ProgName.get()}\\{ProgName.get()}.png')

        with open(f'Apps\\{ProgName.get()}\\{ProgName.get()}.py',"w") as File:
            File.write(coder.get("1.0","end"))

        message.set("[Info]: Saved "+str(ProgName.get())+"!")

    # command buttons
    color_E_button = T.Button(Packer, text='Change Color (Entry)', command= lambda: change_settings(True))
    color_S_button = T.Button(Packer, text='Change Color (Sliders)', command= lambda: change_settings(False))
    saver = T.Button(Packer,text="Save",command=save)

    # gridding
    canvas.grid(row=0,column=0,columnspan=2,sticky="nw",pady=30)
    coder.grid(row=0,column=2,rowspan=5,sticky="ns",pady=30)
    ProgName.grid(row=6,column=0,columnspan=1,sticky="we")
    Error.grid(row=1000,columnspan=3,sticky='we')

    red.grid(row=2,column=0)
    green.grid(row=3,column=0)
    blue.grid(row=4,column=0)

    redSlider.grid(row=2,column=1)
    greenSlider.grid(row=3,column=1)
    blueSlider.grid(row=4,column=1)

    color_E_button.grid(row=5,column=0,sticky='we')
    color_S_button.grid(row=5,column=1,sticky='we')
    saver.grid(row=6,column=1,sticky='we')