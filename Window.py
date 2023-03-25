from tkinter import *
import os
from PIL import Image, ImageTk
import json

from RunHandler import *

def initOS():
    OS = Tk()
    OS.title("PY OS v1.0")
    with open("Sys_Config.json","r") as C:
        Config = json.load(C)
        C.close()

        OS.attributes("-fullscreen",Config["Fullscreen"])
        if Config["Fullscreen"] == False:
            OS.geometry(Config["Resolution"])
        elif Config["Fullscreen"] == True:
            OS.geometry(str(OS.winfo_screenwidth()) + "x" + str(OS.winfo_screenheight()))
        OS.update()
        return OS

def initScreen(OS):
    with open("Sys_Config.json", "r") as config_file:
        config = json.load(config_file)
    res = config["Resolution"].split("x")
    w = int(res[0])
    h = int(res[1])
    config_file.close()

    screen = Canvas(OS, width=w, height=h, bg=config["Wallpaper_Color"])
    screen.pack()
    programbar = screen.create_rectangle(0, h-80, w, h, fill=config["Taskbar_Color"])
    screen_reg = [screen, programbar]
    return screen_reg

def initInfo_Icons(OS):
    with open("Sys_Config.json", "r") as config_file:
        config = json.load(config_file)
    res = config["Resolution"].split("x")
    w = int(res[0])
    h = int(res[1])
    config_file.close()

    Ratio = w/h
    WRatio = (w/Ratio)
    HRatio = (h/Ratio)
    core_iconinfo = [WRatio,HRatio]
    return core_iconinfo

def initSystemPrograms(OS,screen,WRatio,HRatio):
    with open("Sys_Config.json", "r") as config_file:
        config = json.load(config_file)
    res = config["Resolution"].split("x")
    w = int(res[0])
    h = int(res[1])
    config_file.close()

    Size = 64

    imgreg = []
    sysreg = []

    ProgramPath = 'SystemPrograms'

    IconW = Size/4
    IconH = h-(((IconW/2)+Size))

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
        
        if IconW > w:
            break
    
    Sys_Reg = [sysreg,imgreg]
    return Sys_Reg

def initApps(OS, screen, WRatio, HRatio):
    with open("Sys_Config.json", "r") as config_file:
        config = json.load(config_file)
    res = config["Resolution"].split("x")
    w = int(res[0])
    h = int(res[1])
    config_file.close()

    Size = 64

    imgreg = []
    appreg = []

    AppPath = 'Apps'

    IconW = 20
    IconH = Size/4
    
    for File in os.listdir(AppPath):
        imgFile = str(AppPath) + "/" + str(File) + "/" + str(File) + ".png"

        image = Image.open(imgFile)
        image = image.resize((Size, Size))
        icon = ImageTk.PhotoImage(image)
        imgreg.append(icon)

        img_tag = screen.create_image(IconW, IconH, image=icon, anchor=NW)
        app = screen.tag_bind(img_tag, "<Double-Button-1>",lambda event, runnable = str(AppPath) + "." + str(File) + "." + str(File): Run(event,OS,runnable))
        imgreg.append(icon)
        appreg.append(app)

        screen.create_text(IconW+Size/2, IconH+Size, text=str(File), font=("Arial", 12), fill="white", anchor=N)

        IconW += (3*Size/2)
        if IconW > w:
            IconW = 20
            IconH += IconH
        if IconH > (h-Size):
            break
    
    App_Reg = [appreg,imgreg]
    return App_Reg

def initReloader(OS,screen,programbar,core_iconinfo,sys_reg,app_reg):
    with open("Sys_Config.json", "r") as config_file:
        config = json.load(config_file)
    res = config["Resolution"].split("x")
    w = int(res[0])
    h = int(res[1])
    config_file.close()

    Size = 64
    reloader_reg = []
    imgFile = "Reloader.png"

    image = Image.open(imgFile).resize((Size, Size))
    icon = ImageTk.PhotoImage(image)

    img_tag = screen.create_image(w-Size, h-((5*Size)/4), image=icon, anchor=NW)
    rload = screen.tag_bind(img_tag, "<Double-Button-1>",lambda event: Reload(OS,screen,programbar))

    reloader_reg.append(icon)
    reloader_reg.append(rload)

    return reloader_reg