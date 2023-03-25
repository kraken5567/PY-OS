def Main(OS):
    from tkinter import filedialog as Fd
    import tkinter as T
    import os

    FileManager = T.Toplevel()
    FileManager.withdraw()
    FileManager.title("File Manager")
    Location = os.path.abspath(os.path.join(os.getcwd(), ""))
    FileManager.filename = Fd.askopenfilename(initialdir=Location, title="Select A File", filetypes=(("all files", "*.*"),("App/Sys Icons", "*.png"),("Configs","*.json"),("PyOS Runnables","*.py")))
    File = open(FileManager.filename,"r")
    return File.read()