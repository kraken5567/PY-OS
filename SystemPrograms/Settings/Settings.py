def Main():
    import tkinter as Tk
    import json

    Open = True
    while Open == True:
    #Initiate
        settings = "Sys_Config.json"
        Fullscreen_var = Tk.BooleanVar()
        root = Tk.Tk()

        #Window setup!
        Top_Label = Tk.Label(root,text="Settings Menu")

        Fullscreen = Tk.Radiobutton(root,text="Fullscreen",variable=Fullscreen_var,value=True)
        Windowed = Tk.Radiobutton(root,text="Windowed",variable=Fullscreen_var,value=False)

        #functions
        def Exit():
            root.destroy()

        def Apply():
            # Load the configuration from the file
            with open(settings, "r") as f:
                config_json = json.load(f)

            # Update the configuration dictionary
            config_json["Fullscreen"] = Fullscreen_var.get()

            # Save the updated configuration to the file
            with open(settings, "w") as f:
                json.dump(config_json, f)
                print("applied!")
        
        #function runners
        apply = Tk.Button(root,text="Apply Settings",command=Apply)
        exit = Tk.Button(root,text="Exit",command=Exit)

        #The Packening!
        Top_Label.pack()
        Fullscreen.pack()
        Windowed.pack()
        

        apply.pack()
        exit.pack()

        
        
        #Always Last!
        root.mainloop()