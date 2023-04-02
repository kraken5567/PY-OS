def Main(OS):
    import tkinter as T
    import os
    import importlib.util

    paper = T.Toplevel(OS)
    paper.title("File Editor")
    paper.columnconfigure(0, weight=1)
    paper.rowconfigure(0, weight=1)

    h = 20
    code_vis = T.Text(paper,height=h,font=8)
    for x in range(h):
        code_vis.insert(f"{x+1}.0","\n")
    T.Scrollbar(code_vis)
    code_vis.grid(row=0,columnspan=3)

    def Exit():
        paper.destroy()
    exit = T.Button(paper,text="Exit",bg="red",command=Exit)
    exit.grid(row=2, column=2, padx=10, pady=10, sticky='e')

    def Apply():
        import SystemPrograms.FileFinder.FileFinder as FF
        importlib.reload(FF)
        Folder = FF.FFImported(OS)
        code = code_vis.get("1.0", "end-1c")
        with open(os.path.join(Folder,name.get()),"w") as File:
            File.write(code)
    apply = T.Button(paper,text="Save",bg="blue",command=Apply)
    apply.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    name = T.Entry(paper,width=64)
    name.insert(0,".txt")
    name.grid(row=2,column=1,sticky='we')

    paper.mainloop()



def ReadEdit(OS,select,Location):
    import tkinter as T
    import os

    paper = T.Toplevel(OS)
    paper.title("File Editor")
    paper.columnconfigure(0, weight=1)
    paper.rowconfigure(0, weight=1)

    code_vis = T.Text(paper,height=20,font=8)
    T.Scrollbar(code_vis)

    place = os.path.join(Location, select)
    with open(place, "r") as File:
        file = File.read()
        lines = file.split("\n")
        for row, line in enumerate(lines):
            code_vis.insert(f"{row+1}.0", line + "\n")
        code_vis.grid(row=0, columnspan=3, padx=10, pady=10, sticky='we')
        paper.columnconfigure(0, weight=1)

        def Exit():
            paper.destroy()
        exit = T.Button(paper,text="Exit",bg="red",command=Exit)
        exit.grid(row=2, column=2, padx=10, pady=10, sticky='e')

        def Apply():
            code = code_vis.get("1.0", "end-1c")
            with open(os.path.join(Location, select), "w") as file:
                file.write(code)
        apply = T.Button(paper,text="Save",bg="blue",command=Apply)
        apply.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        name = T.Entry(paper,width=64)
        name.grid(row=2,column=1,sticky='we')

        paper.mainloop()
