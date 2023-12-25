def Main(OS):
    import SystemPrograms.FileFinder.FileFinder as FF
    import importlib.util
    
    importlib.reload(FF)
    
    Loc = FF.FFImported(OS)
    coder(Loc,OS)
    
def coder(fileDir,OS):
    import tkinter as T
    from PIL import ImageTk, Image
    from WindowsClass import MovableFrame as MF

    ProgDir = "Apps"
    ProgFolder = "PyOSCoder"

    #put icon in frame
    icon = Image.open(f"{ProgDir}\\{ProgFolder}\\{ProgFolder}.png")

    Frame = MF(OS, icon, [750, 300])
    Coder = Frame.frame
    
    code_vis = T.Text(Coder,height=20,font=8)
    T.Scrollbar(code_vis)
    file = open(fileDir, "r")
    file = file.read()
    lines = file.split("\n")
    for row, line in enumerate(lines):
        code_vis.insert(f"{row+1}.0", line + "\n")
    code_vis.grid(row=1, columnspan=3, padx=10, pady=30, sticky='we')

    def Apply():
        code = code_vis.get("1.0", "end-1c")
        with open(fileDir, "w") as file:
            file.write(code)
    
    apply = T.Button(Coder,text="Save",bg="blue",command=Apply)
    apply.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    
    Coder.mainloop()
    del Coder