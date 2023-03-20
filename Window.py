from tkinter import *
import os
from PIL import Image, ImageTk
import json

from RunHandler import *



def initOS():
    OS = Tk()
    OS.title("PY OS v0.0")
    Config = json.load(open("Sys_Config.json","r"))
    Resolution = Config["Resolution"]
    OS.attributes("-fullscreen",Config["Fullscreen"])
    print(Config["Fullscreen"])
    if Config["Fullscreen"] in "False":
        OS.geometry(Resolution[0] + "x" + Resolution[1])
        print(Resolution[0] + "x" + Resolution[1])
    else:
        OS.geometry(str(OS.winfo_screenwidth()) + "x" + str(OS.winfo_screenwidth()))
    OS.update()
    return OS

def initScreen(OS):
    W = OS.winfo_width()
    H = OS.winfo_height()
    print(W,H)
    screen = Canvas(OS,width=W,height=H,bg="dark blue")
    screen.pack()
    programbar = screen.create_rectangle(0,H-80,W,H,fill="gray")
    return screen

def initInfo_Icons(OS):
    
    Ratios = [[4,3],[16,9],[5,4],[1,1],[3,4],[9,16],[4,5],[1,1]]
    for x in Ratios:
        if (OS.winfo_width()/OS.winfo_height()) == (x[0]/x[1]):
            WRatio = (OS.winfo_width()/x[0])/2
            HRatio = (OS.winfo_height()/x[1])/2
    core_iconinfo = [WRatio,HRatio]
    return core_iconinfo

def initSystemPrograms(OS,screen,WRatio,HRatio):
    Size = 64

    imgreg = []
    sysreg = []

    ProgramPath = 'SystemPrograms'

    IconW = Size/4
    IconH = OS.winfo_height()-((IconW/2)+Size)
    
    print("Sys initialized!",IconW,IconH)

    for File in os.listdir(ProgramPath):

        imgFile = str(ProgramPath) + "/" + str(File) + "/" + str(File) + ".png"

        if os.path.exists(imgFile):
            print("Exists!")

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
    IconH = HRatio/2
    
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