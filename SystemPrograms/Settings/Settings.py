def Main(OS):
    from tkinter import BooleanVar, Radiobutton, Label, Entry, Button, Toplevel, X, Y, StringVar
    import json as J

    print("Settings Ran!")
    Setting_Frame = Toplevel()

    
    Fullscreen = BooleanVar()
    #Resolution, Wallpaper_Color, and TaskBar_Color are all entries
    

    with open("Sys_Config.json","r") as R_cfg:
        cfg_r = J.load(R_cfg)

        Fullscr = Radiobutton(Setting_Frame, text="Fullscreen", variable=Fullscreen, value = True)
        Windowed = Radiobutton(Setting_Frame, text="Windowed", variable=Fullscreen, value = False)
        
        RLabel = Label(Setting_Frame,text="Resolution(WxH)")
        Resolution = Entry(Setting_Frame)
        Resolution.insert(0,cfg_r["Resolution"])

        TBarLabel = Label(Setting_Frame,text="Taskbar's Color")
        Taskbar_Color = Entry(Setting_Frame)
        Taskbar_Color.insert(0,cfg_r["Taskbar_Color"])

        WPLabel = Label(Setting_Frame,text="Wallpaper's Color")
        Wallpaper_Color = Entry(Setting_Frame)
        Wallpaper_Color.insert(0,cfg_r["Wallpaper_Color"])



        
        Fullscr.grid(row=1, column=0)
        Windowed.grid(row=1, column=1)

        RLabel.grid(row=2,column=0, columnspan=2)
        Resolution.grid(row=3, column=0, columnspan=2)

        TBarLabel.grid(row=4, column=0)
        Taskbar_Color.grid(row=4, column=1)

        WPLabel.grid(row=5, column=0)
        Wallpaper_Color.grid(row=5, column=1)

        def Apply():
            with open("Sys_Config.json", "r") as R_cfg:
                cfg = J.load(R_cfg)
                for k in cfg:
                    if k == "Fullscreen":
                        cfg[k] = Fullscreen.get()
                    elif k == "Resolution":
                        cfg[k] = Resolution.get()
                    elif k == "Taskbar_Color":
                        cfg[k] = Taskbar_Color.get()
                    elif k == "Wallpaper_Color":
                        cfg[k] = Wallpaper_Color.get()
                with open("Sys_Config.json", "w") as W_cfg:
                    J.dump(cfg, W_cfg)

        def Exit():
            Setting_Frame.destroy()

        # Bottom Buttons
        apply = Button(Setting_Frame,text="Apply Settings",bg="green",command=Apply)
        exit = Button(Setting_Frame,text="          Exit          ",bg="red",command=Exit)

        apply.grid(row=6,column=0)
        exit.grid(row=6,column=1)

        OS.mainloop()