from tkinter import *
import os
from PIL import Image, ImageTk
import json

from RunHandler import *

def initOS():
    OS = Tk()
    OS.title("PY OS v0.0")
    Config = json.load(open("Sys_Config.json","r"))
    OS.attributes("-fullscreen",Config["Fullscreen"])
    if Config["Fullscreen"] == False:
        OS.geometry(Config["Resolution"])
    elif Config["Fullscreen"] == True:
        OS.geometry(str(OS.winfo_screenwidth()) + "x" + str(OS.winfo_screenheight()))
    OS.update()
    return OS

def initScreen(OS):
    Config = json.load(open("Sys_Config.json","r"))
    W = OS.winfo_width()
    H = OS.winfo_height()
    screen = Canvas(OS,width=W,height=H,bg=Config["Wallpaper_Color"])
    screen.pack()
    programbar = screen.create_rectangle(0,H-80,W,H,fill=Config["Taskbar_Color"])
    screen_reg = [screen,programbar]
    return screen_reg

def initInfo_Icons(OS):
    Ratio = OS.winfo_width()/OS.winfo_height()
    WRatio = (OS.winfo_width()/Ratio)
    HRatio = (OS.winfo_height()/Ratio)
    core_iconinfo = [WRatio,HRatio]
    return core_iconinfo

def initSystemPrograms(OS,screen,WRatio,HRatio):
    Size = 64

    imgreg = []
    sysreg = []

    ProgramPath = 'SystemPrograms'

    IconW = Size/4
    IconH = OS.winfo_height()-(((IconW/2)+Size))

    for File in os.listdir(ProgramPath):

        imgFile = str(ProgramPath) + "/" + str(File) + "/" + str(File) + ".png"

        image = Image.open(imgFile)
        image = image.resize((Size, Size))
        icon = ImageTk.PhotoImage(image)

        img_tag = screen.create_image(IconW, IconH, image=icon, anchor=NW)
        sys = screen.tag_bind(img_tag, "<Button-1>",lambda event, runnable = str(ProgramPath) + "." + str(File) + "." + str(File): Run(event,OS,runnable))
        imgreg.append(icon)
        sysreg.append(sys)
        
        IconW += (5*Size/4)
        
        if IconW > OS.winfo_width():
            break
    
    Sys_Reg = [sysreg,imgreg]
    return Sys_Reg

def initApps(OS, screen, WRatio, HRatio):
    Size = 64

    imgreg = []
    appreg = []

    AppPath = 'Apps'

    IconW = 20
    IconH = Size/4
    
    for File in os.listdir(AppPath):

        imgFile = str(AppPath) + "/" + str(File) + "/" + str(File) + ".png"

        if os.path.exists(imgFile):
            print("Exists!")

        image = Image.open(imgFile)
        image = image.resize((Size, Size))
        icon = ImageTk.PhotoImage(image)
        imgreg.append(icon)

        img_tag = screen.create_image(IconW, IconH, image=icon, anchor=NW)
        app = screen.tag_bind(img_tag, "<Double-Button-1>",lambda event, runnable = str(AppPath) + "." + str(File) + "." + str(File): Run(event,OS,runnable))
        imgreg.append(icon)
        appreg.append(app)

        screen.create_text(IconW+Size/2, IconH+Size, text=str(File), font=("Arial", 16), fill="white", anchor=N)

        IconW += WRatio
        if IconW > OS.winfo_width():
            IconW = 20
            IconH += HRatio
        if IconH > (OS.winfo_height()-Size):
            break
    
    App_Reg = [appreg,imgreg]
    return App_Reg

def initReloader(OS,screen,programbar,core_iconinfo,sys_reg,app_reg):
    Size = 64
    reloader_reg = []
    imgFile = "Reloader.png"
    image = Image.open(imgFile).resize((Size, Size))
    icon = ImageTk.PhotoImage(image)

    img_tag = screen.create_image(OS.winfo_width()-Size, OS.winfo_height()-((5*Size)/4), image=icon, anchor=NW)
    rload = screen.tag_bind(img_tag, "<Double-Button-1>",lambda event: Reload(OS,screen,programbar))

    reloader_reg.append(icon)
    reloader_reg.append(rload)

    return reloader_reg