def Main(OS):
    import tkinter as T
    import os
    import importlib.util

    selection = T.StringVar()

    def ReadFolderContents(Location):
        fileFolderList = os.listdir(Location)
        return fileFolderList
    
    FileManager = T.Toplevel()
    FileManager.title("File Manager")
    Location = os.getcwd()

    lister = T.Label(FileManager,text=Location)
    T.Scrollbar(lister)

    contents = ReadFolderContents(Location)

    allRButtons = []
    for x, y in enumerate(contents):
        if ("." in y[-5:]) and not ("." in y[:1]):
            a = T.Radiobutton(FileManager, text = y, variable = selection, value = y, bg="blue")
        else:
            a = T.Radiobutton(FileManager, text = y, variable = selection, value = y,bg="yellow")
        a.grid(row=x+1,column=0,sticky='we')
        allRButtons.append(a)

    lister.grid(row=0,column=1)
    #button functions

    #File stuff
    def OpenFile(select,Location):
        if select.endswith((".png","jpg","jpeg",".gif",".bmp",".tif",".tiff")):
            print("Not Yet Implemented, Soon though")
        elif not select.endswith((".png","jpg","jpeg",".gif",".bmp",".tif",".tiff")):
            import SystemPrograms.Noterer.Noterer as Nt
            importlib.reload(Nt)
            Nt.ReadEdit(select,Location)
            del Nt
    #def NewFile(select,Location):
    #def EditFile(select,Location):

    #Folder Stuff
    #def OpenFolder(select,Location):
    #def NewFolder(select,Location):



    #buttons
    buttonList = ["OpenFile"]#,"NewFile","EditFile","OpenFolder","NewFolder"]
    funcList = [OpenFile]#,NewFile,EditFile,OpenFolder,NewFolder]
    y = 0
    z = 0
    n = 0
    for x in buttonList:
        B = T.Button(FileManager, text=str(x), command=lambda f=funcList[n]: f(selection.get(), Location))
        B.grid(row=z+8, column=y+1, sticky='we')
        y += 1
        if y > 6:
            y = 0
            z += 1
        n += 1

    

def FFImported():
    from tkinter import filedialog as Fd
    import tkinter as T
    import os

    FileManager = T.Toplevel()
    FileManager.withdraw()
    FileManager.title("File Manager")
    Location = os.path.abspath(os.getcwd())
    FileManager.filename = Fd.askopenfilename(initialdir=Location, title="Select A File", filetypes=(("all files", "*.*"),("App/Sys Icons", "*.png"),("Configs","*.json"),("PyOS Runnables","*.py")))
    File = open(FileManager.filename,"r")

    return File.read()