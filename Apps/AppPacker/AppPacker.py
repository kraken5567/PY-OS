def Main(OS):
    import PIL.ImageGrab as ImageGrab
    from PIL import ImageTk, Image
    import tkinter as T
    import json as J
    import os
    import math

    with open("Sys_Config.json","r") as C:
        Config = J.load(C)
        C.close()
    
    Res = Config["Resolution"].split("x")
    w = int(Res[0])
    h = int(Res[1])

    d = T.IntVar(value=128)
    imageres = T.IntVar(value=16)
    brush_size = d.get()//imageres.get()

    color_hex = T.StringVar(value='#FFFFFF')
    message = T.StringVar()

    Packer = T.Toplevel(OS,width=w,height=h)
    Packer.transient(OS)
    Packer.title("App Packer")
    ProgDir = "Apps"
    ProgFolder = "AppPacker"
    icon = ImageTk.PhotoImage(Image.open(f"{ProgDir}\\{ProgFolder}\\{ProgFolder}.png"))
    Packer.iconphoto(False, icon)

    canvas = T.Canvas(Packer,bg="white",height=d.get(),width=d.get())
    canvas.grid(row=0,column=0,sticky="nw")

    coder = T.Text(Packer, bg="light gray", width=100)
    coder.grid(row=0,column=1,rowspan=5,sticky="ns")
    coder.insert("1.0","def Main(OS): \n import tkinter as T \n from PIL import ImageTk, Image \n App = T.Toplevel(OS) \n App.transient(OS) \n App.title('Packed App') \n ProgDir = 'Apps' \n ProgFolder = #put app name here \n icon = ImageTk.PhotoImage(Image.open(f'{ProgDir}\\{ProgFolder}\\{ProgFolder}.png')) \n App.iconphoto(False, icon)")

    icon = ImageTk.PhotoImage(Image.open(f"{ProgDir}\\{ProgFolder}\\{ProgFolder}.png"))

    ProgName = T.Entry(Packer,bg="light gray")
    ProgName.grid(row=6,column=0,columnspan=1,sticky="we")
    ProgName.insert(0,"App")

    Error = T.Label(Packer,fg="red",bg="black",textvariable=message)
    Error.grid(row=1000,columnspan=3,sticky='we')

    #brush settings
    global brush_color
    brush_color = (0, 0, 0) 
    #rgb inputs
    red = T.Entry(Packer,bg="red")
    red.insert(0,0)
    green = T.Entry(Packer,bg="green")
    green.insert(0,0)
    blue = T.Entry(Packer,bg="blue")
    blue.insert(0,0)

    def change_settings():
        global brush_color
        r_val = int(red.get())
        g_val = int(green.get())
        b_val = int(blue.get())
        brush_color = (r_val, g_val, b_val)
        
    def paint(event,red,green,blue):
        x, y = event.x, event.y
        row, col = x // brush_size, y // brush_size
        x1, y1 = row * brush_size, col * brush_size
        x2, y2 = x1 + brush_size, y1 + brush_size
        (red, green, blue) = brush_color
        global color_hex
        color_hex = f'#{red:02x}{green:02x}{blue:02x}'  #RGB to Hex
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_hex, outline=color_hex)
    canvas.bind('<B1-Motion>', lambda event: paint(event,red.get(),green.get(),blue.get()))

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
    color_button = T.Button(Packer, text='Change Settings', command=change_settings, bg=color_hex.get())
    saver = T.Button(Packer,text="Save",command=save)

    red.grid(row=2,column=0)
    green.grid(row=3,column=0)
    blue.grid(row=4,column=0)
    color_button.grid(row=5,column=0,sticky='we')
    saver.grid(row=6,column=1,sticky='we')