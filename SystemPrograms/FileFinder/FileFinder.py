def Main(OS):
    import tkinter as T
    import os
    import importlib.util

    selection = T.StringVar()

    FileManager = T.Toplevel(OS)
    FileManager.title("File Manager")
    FileManager.transient(OS)

    # Evil Global
    global Location
    Location = os.getcwd()
    #--------------------

    lister = T.Label(FileManager)
    lister.config(text=Location)
    lister.grid(row=0,columnspan=3,sticky='we')

    Error = T.Label(FileManager,fg="red",bg="black")
    Error.grid(row=1000,columnspan=3,sticky='we')

    # functions
    def ReadFolderContents():
        global Location
        lister.config(text=Location)
        fileFolderList = os.listdir(Location)
        return fileFolderList

    def updateContents():
        contents = ReadFolderContents()
        allRButtons = []
        for x, y in enumerate(contents):
            if ("." in y[-5:]) and not ("." in y[:1]):
                a = T.Radiobutton(FileManager, text = y, variable = selection, indicatoron=0, value = y, bg="blue",fg="Red")
            else:
                a = T.Radiobutton(FileManager, text = y, variable = selection, indicatoron=0, value = y,bg="yellow",fg="red")
            a.grid(row=x+1,column=0,sticky='we')
            allRButtons.append(a)
            
        return allRButtons


    global allRButtons
    allRButtons = updateContents()


    # file stuff
    def OpenFile(select):
        global Location
        if select.endswith((".png","jpg","jpeg",".gif",".bmp",".tif",".tiff")):
            import SystemPrograms.Painter.Painter as Pnt
            importlib.reload(Pnt)
            Pnt.redraw(OS,select,Location)
        elif not select.endswith((".png","jpg","jpeg",".gif",".bmp",".tif",".tiff")):
            import SystemPrograms.Noterer.Noterer as Nt
            importlib.reload(Nt)
            Nt.ReadEdit(OS,select,Location)
            del Nt
    
    def NewFile(select):
        global Location
        if not os.path.exists(os.path.join(Location, NewItem.get())):
            with open(os.path.join(Location, NewItem.get()), 'w') as NewFile:
                NewFile.write("")
                NewFile.close()

    #Folder Stuff
    def OpenFolder(select):
        global Location
        Location = os.path.join(Location, select)
        global allRButtons
        for x in allRButtons:
            x.destroy()
        allRButtons = updateContents()
        return Location

    def NewFolder(select):
        global Location
        if not os.path.exists(os.path.join(Location, NewItem.get())):
            os.mkdir(os.path.join(Location, NewItem.get()))

    # button stuff
    buttonList = ["OpenFile","NewFile","OpenFolder","NewFolder"]
    funcList = [OpenFile,NewFile,OpenFolder,NewFolder]
    y = 0
    z = 0
    n = 0
    for x in buttonList:
        B = T.Button(FileManager, text=str(x), command=lambda f=funcList[n]: f(selection.get()))
        B.grid(row=z+1, column=y+1, sticky='we')
        y += 1
        if y >= 2:
            y = 0
            z += 1
        n += 1

    EntryLabel = T.Label(FileManager,text="Entry for 'New' Items")
    EntryLabel.grid(row=z+1,column=1,columnspan=2)

    NewItem= T.Entry(FileManager)
    NewItem.grid(row=z+2,column=1,columnspan=2)

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