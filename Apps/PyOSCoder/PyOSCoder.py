def Main(OS):
    import SystemPrograms.FileFinder.FileFinder as FF
    import importlib.util
    
    importlib.reload(FF)
    
    Loc = FF.FFImported(OS)
    coder(Loc)
    
def coder(fileDir):
    import tkinter as T
    from PIL import ImageTk, Image

    Coder = T.Toplevel()
    Coder.title("PyOS Coder")
    ProgDir = "Apps"
    ProgFolder = "PyOSCoder"
    icon = ImageTk.PhotoImage(Image.open(f"{ProgDir}\\{ProgFolder}\\{ProgFolder}.png"))
    Coder.iconphoto(False, icon)
    

    code_vis = T.Text(Coder,height=20,font=8)
    T.Scrollbar(code_vis)
    file = open(fileDir, "r")
    file = file.read()
    lines = file.split("\n")
    for row, line in enumerate(lines):
        code_vis.insert(f"{row+1}.0", line + "\n")
    code_vis.grid(row=0, columnspan=3, padx=10, pady=10, sticky='we')
    Coder.columnconfigure(0, weight=1)

    def Exit():
        Coder.destroy()
    exit = T.Button(Coder,text="Exit",bg="red",command=Exit)
    exit.grid(row=2, column=2, padx=10, pady=10, sticky='e')

    def Apply():
        code = code_vis.get("1.0", "end-1c")
        with open(fileDir, "w") as file:
            file.write(code)
    apply = T.Button(Coder,text="Save",bg="blue",command=Apply)
    apply.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    Coder.mainloop()