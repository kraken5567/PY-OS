def Main(OS):
    from tkinter import BooleanVar, Radiobutton, IntVar, Label, Entry, Button, Toplevel, X, Y, END
    import json as J
    import importlib.util
    import os
    from PIL import ImageTk, Image

    import SystemPrograms.FileFinder.FileFinder as FF
    from WindowsClass import MovableFrame as MF

    ProgDir = "SystemPrograms"
    ProgFolder = "Settings"

    Frame = MF(OS,Image.open(f"{ProgDir}\\{ProgFolder}\\{ProgFolder}.png"),[750,300])

    Setting_Frame = Frame.frame

    Fullscreen = BooleanVar()
    
    #Resolution, Wallpaper_Color/Image, and TaskBar_Color are all entries

    with open("Sys_Config.json","r") as R_cfg:
        cfg_r = J.load(R_cfg)
        R_cfg.close()

        Fullscr = Radiobutton(Setting_Frame, text="Fullscreen", variable=Fullscreen, value = True)
        Windowed = Radiobutton(Setting_Frame, text="Windowed", variable=Fullscreen, value = False)
        
        RLabel = Label(Setting_Frame,text="Resolution(WxH)")
        Resolution = Entry(Setting_Frame)
        Resolution.insert(0,cfg_r["Resolution"])

        TBarLabel = Label(Setting_Frame,text="Taskbar's Color")
        Taskbar_Color = Entry(Setting_Frame)
        Taskbar_Color.insert(0,cfg_r["Taskbar_Color"])
        if "/" in cfg_r["Wallpaper"]:
            WallpaperFormat = IntVar(value="Wallpaper Image")
        else:
            WallpaperFormat = IntVar(value="Wallpaper Color")

        WPCLabel = Radiobutton(Setting_Frame,text="Wallpaper's Color",variable=WallpaperFormat,value=0)
        WPILabel = Radiobutton(Setting_Frame,text="Wallpaper Image",variable=WallpaperFormat,value=1)
        Wallpaper = Entry(Setting_Frame)
        Wallpaper.insert(0,cfg_r["Wallpaper"])
        
        

        
        Fullscr.grid(row=1, column=0, pady=(30,0))
        Windowed.grid(row=1, column=1, pady=(30,0))

        RLabel.grid(row=2,column=0, columnspan=2)
        Resolution.grid(row=3, column=0, columnspan=2)

        TBarLabel.grid(row=4, column=0)
        Taskbar_Color.grid(row=4, column=1)

        WPCLabel.grid(row=5, column=0)
        WPILabel.grid(row=5, column=1)
        Wallpaper.grid(row=6, column=0)

        def ImageLocation():
            importlib.reload(FF)
            File = FF.FFImported(OS)
            WallpaperFormat.set(value="Wallpaper Image")
            File = os.path.relpath(File, os.getcwd())
            Wallpaper.delete(0,END)
            Wallpaper.insert(0,File)

        fileLoc = Button(Setting_Frame,text="Select Image",command=ImageLocation)
        fileLoc.grid(row=6, column=1)

        def Apply():
            with open("Sys_Config.json", "r") as R_cfg:
                cfg = J.load(R_cfg)
                R_cfg.close()

                for k in cfg:
                    if k == "Fullscreen":
                        cfg[k] = Fullscreen.get()
                    elif k == "Resolution":
                        cfg[k] = Resolution.get()
                    elif k == "Taskbar_Color":
                        cfg[k] = Taskbar_Color.get()
                    elif k == "Wallpaper":
                        cfg[k] = Wallpaper.get()
                with open("Sys_Config.json", "w") as W_cfg:
                    J.dump(cfg, W_cfg)

        def Exit():
            Setting_Frame.destroy()

        # Bottom Buttons
        apply = Button(Setting_Frame,text="Apply Settings",bg="green",command=Apply)
        exit = Button(Setting_Frame,text="          Exit          ",bg="red",command=Exit)

        apply.grid(row=9,column=0)
        exit.grid(row=9,column=1)

        OS.mainloop()