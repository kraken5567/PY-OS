def Main():
    import tkinter as Tk
    #Initiate
    print("Settings Ran!")
    txt = "SystemPrograms\Settings\Settings.txt"
    Read = open(txt,"r")
    root = Tk.Tk()

    Write = open(txt,"w")

    #Window setup!
    Top_Label = Tk.Label(text="Settings Menu")
    Fullscreen = Tk.Radiobutton(text="Fullscreen")
    Windowed = Tk.Radiobutton(text="Windowed")


    #The Packening!
    Top_Label.pack()
    Fullscreen.pack()
    Windowed.pack()

    #Always Last!
    root.mainloop()