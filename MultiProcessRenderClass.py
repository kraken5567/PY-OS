from PIL import Image, ImageTk
import tkinter as tk
import math

class Gif:
    def __init__(self, canvas, gif_path):
        self.canvas = canvas
        self.gif_path = gif_path
        self.gif_index = 0
        self.gif_frames = []

        self.load_gif()

    def load_gif(self):
        self.gif_frames = []
        with Image.open(self.gif_path) as gif:
            for frame in range(gif.n_frames):
                gif.seek(frame)
                frame_image = gif.resize((self.canvas.winfo_width(), self.canvas.winfo_height()), Image.ANTIALIAS)
                frame_image = ImageTk.PhotoImage(frame_image)
                self.gif_frames.append(frame_image)

        # create a canvas image object and add it to the canvas
        self.canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.gif_frames[0])
        self.canvas.tag_lower(self.canvas_image)  # move the gif to the bottom of the canvas stack

        self.update()

    def update(self):
        self.gif_index += 1

        if self.gif_index >= len(self.gif_frames):
            self.gif_index = 0

        self.canvas.itemconfig(self.canvas_image, image=self.gif_frames[self.gif_index])

        self.canvas.after(math.trunc(350/len(self.gif_frames)))
