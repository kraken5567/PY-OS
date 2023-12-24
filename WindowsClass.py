import tkinter as tk
from PIL import ImageTk

class MovableFrame:

    # frame
    root = None
    icon = None

    frame = None
    titlebar = None
    icon_label = None

    # Variables for dragging
    lastMoveX = 0
    lastMoveY = 0
    mouseDown = False

    start_x = 50
    start_y = 50

    X = 100
    Y = 100

    def drag(self):
        if self.mouseDown:
            delta_x = self.root.winfo_pointerx() - self.start_x
            delta_y = self.root.winfo_pointery() - self.start_y
            new_x = self.frame.winfo_x() + delta_x
            new_y = self.frame.winfo_y() + delta_y
            self.frame.place(x=new_x, y=new_y)
            self.start_x = self.root.winfo_pointerx()
            self.start_y = self.root.winfo_pointery()
            self.after_id = self.root.after(1, self.drag)

    def start_drag(self, event):
        if self.isDrag(event):
            self.mouseDown = True
            self.start_x = self.root.winfo_pointerx()
            self.start_y = self.root.winfo_pointery()
            self.drag()

    def stop_drag(self, event):
        self.mouseDown = False
        if hasattr(self, 'after_id'):
            self.root.after_cancel(self.after_id)

    def isDrag(self, event):

        #current_x = self.frame.winfo_rootx(); edge_x = current_x + self.X
        #current_y = self.frame.winfo_rooty(); edge_y = current_y + self.Y

        #print(f"{0} <= {event.x} <= {self.X} * {0} <= {event.y} <= {self.titlebar.winfo_height()} = {(0 <= event.x <= self.X) and (0 <= event.y <= self.titlebar.winfo_height())}"  )
        if (0 <= event.x <= self.X) and (0 <= event.y <= self.titlebar.winfo_height()):
            return True
        else:
            return False
    
    def __init__(self, root, icon, size):
        self.X, self.Y = size

        self.root = root
        self.icon = icon

        self.frame = tk.Frame(root, width=self.X, height=self.Y, bg='white')
        self.frame.place(x=self.start_x, y=self.start_y)

        self.titlebar = tk.Frame(self.frame, height=30, bg='gray')
        self.titlebar.place(relx=0, rely=0, relwidth=1, anchor='nw')
        self.titlebar.bind("<ButtonPress-1>", self.start_drag)
        self.titlebar.bind("<ButtonRelease-1>", self.stop_drag)

        # Icon
        self.icon = ImageTk.PhotoImage(self.icon.resize((30,30)))
        self.icon_label = tk.Label(self.titlebar, image=self.icon, width=30, height=30, bg='black')
        self.icon_label.place(x=5, y=5)

        # Close button
        close_button = tk.Button(self.titlebar, text='X', command=self.frame.destroy, bg='red', relief='flat')
        close_button.place(relx=1, rely=0, x=-5, y=5, anchor='ne')