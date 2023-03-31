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
    buttonList = ["Open File","New File","Open Folder","New Folder"]
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

def FFImported(OS):
    import tkinter as T
    import os
    import importlib.util

    selection = T.StringVar()
    global FileManager
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
            pass
        elif not select.endswith((".png","jpg","jpeg",".gif",".bmp",".tif",".tiff")):
            import Apps.PyOSCoder.PyOSCoder as Coder
            importlib.reload(Coder)
            Coder.coder(os.path.join(Location, select))

            

    #Folder Stuff
    def OpenFolder(select):
        global Location
        Location = os.path.join(Location, select)
        global allRButtons
        for x in allRButtons:
            x.destroy()
        allRButtons = updateContents()
        return Location


    # button stuff
    buttonList = ["Open File","Open Folder",]
    funcList = [OpenFile,OpenFolder,]
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

    FileManager.mainloop()