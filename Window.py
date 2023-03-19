from tkinter import *
import os
from PIL import Image, ImageTk

from RunHandler import *



def initOS():
    OS = Tk()
    OS.title("PY OS v0.0")
    OS.attributes("-fullscreen",True)
    
    return OS

def initScreen(OS):
    W = OS.winfo_screenwidth()
    H = OS.winfo_screenheight()
    screen = Canvas(OS,width=W,height=H,bg="dark blue")
    screen.pack()
    programbar = screen.create_rectangle(0,H-80,W,H,fill="gray")
    return screen

def initInfo_Icons(OS):
    
    Ratios = [[4,3],[16,9],[5,4],[1,1],[3,4],[9,16],[4,5],[1,1]]
    for x in Ratios:
        if (OS.winfo_screenwidth()/OS.winfo_screenheight()) == (x[0]/x[1]):
            WRatio = (OS.winfo_screenwidth()/x[0])/2
            HRatio = (OS.winfo_screenheight()/x[1])/2
    core_iconinfo = [WRatio,HRatio]
    return core_iconinfo

def initSystemPrograms(OS,screen,WRatio,HRatio):
    Size = 64

    imgreg = []
    sysreg = []

    ProgramPath = 'SystemPrograms'

    IconW = Size/4
    IconH = OS.winfo_screenheight()-((IconW/2)+Size)
    
    print("Sys initialized!",IconW,IconH)

    for File in os.listdir(ProgramPath):

        imgFile = str(ProgramPath) + "/" + str(File) + "/" + str(File) + ".png"

        if os.path.exists(imgFile):
            print("Exists!")

        image = Image.open(imgFile)
        image = image.resize((Size, Size))
        icon = ImageTk.PhotoImage(image)

        img_tag = screen.create_image(IconW, IconH, image=icon, anchor=NW)
        screen.tag_bind(img_tag, "<Double-Button-1>",lambda event: Run(event,OS,str(ProgramPath) + "." + str(File) + "." + str(File)))
        imgreg.append(icon)
        
        IconW += WRatio
        
        if IconW > OS.winfo_screenwidth():
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
        screen.tag_bind(img_tag, "<Double-Button-1>",lambda event: Run(event,OS,str(AppPath) + "." + str(File) + "." + str(File)))
        imgreg.append(icon)

        screen.create_text(IconW+Size/2, IconH+Size, text=str(File), font=("Arial", 16), fill="white", anchor=N)

        IconW += WRatio
        if IconW > OS.winfo_screenwidth():
            IconW = 20
            IconH += HRatio
        if IconH > OS.winfo_screenheight():
            break
    
    App_Reg = [appreg,imgreg]
    return App_Reg