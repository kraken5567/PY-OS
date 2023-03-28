def Main(OS):
    import tkinter as T
    from tkinter import filedialog as fd
    import SystemPrograms.FileFinder.FileFinder as FF
    Coder = T.Toplevel()
    Coder.title("PyOS Coder")

    file_text = FF.FFImported()

    code_vis = T.Text(Coder,height=20,font=8)
    T.Scrollbar(code_vis)

    lines = file_text.split("\n")
    for row, line in enumerate(lines):
        code_vis.insert(f"{row+1}.0", line + "\n")
    code_vis.grid(row=0, column=0, padx=10, pady=10, sticky='we')
    Coder.columnconfigure(0, weight=1)

    def Exit():
        Coder.destroy()
    exit = T.Button(Coder,text="Exit",bg="red",command=Exit)
    exit.grid(row=2, column=1, padx=10, pady=10, sticky='e')

    def Apply():
        code = code_vis.get("1.0", "end-1c")
        code_name = fd.asksaveasfilename(defaultextension=".py",filetypes=[("Python Files", "*.py"),("Json Files", "*.json"),("Text Files", "*.txt"), ("All Files", "*.*")])
        if code_name:
            with open(code_name, "w") as file:
                file.write(code)
    apply = T.Button(Coder,text="Save",bg="blue",command=Apply)
    apply.grid(row=2, column=0, padx=10, pady=10, sticky='w')

    Coder.mainloop()