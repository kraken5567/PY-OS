def Main(OS):
    import tkinter as T
    import SystemPrograms.FileFinder.FileFinder as FF
    Coder = T.Toplevel()
    Coder.title("PyOS Coder")

    file_text = FF.Main(OS)
    lines = file_text.count('\n') 

    #display the file as T.Text
    # cut every line at "\n" and put in a list (item/line)
    # allow editing and resubmission of the line
        # redisplay the text based on edits
    # allow running of the program
        #Run or Customized Run

    # Done

    CodeBox = T.Entry(Coder,width=Coder.winfo_width())
    CodeBox.insert(0,str(file_text))
    CodeBox.grid(row=0, column=0, padx=10, pady=10, sticky='we')
    Coder.columnconfigure(0, weight=1)

    def Exit():
        Coder.destroy()
    exit = T.Button(Coder,text="          Exit          ",bg="red",command=Exit)
    exit.grid(row=1, column=0, padx=10, pady=10)

    Coder.mainloop()