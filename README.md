# Current Tasks
https://trello.com/b/iv365uEC/py-os-dev-to-do

# PY-OS

![pyos-animated-background-pixilart (1)](https://user-images.githubusercontent.com/64876071/229265520-f9fd9ca4-d309-4c2a-8957-aea27070f23d.gif)

Python Based Faux-Operating System

Yes, you can code python in this.

However if you want to run things without restarting reload your modules!

Import, Code, run games!
Nothing is the limit (except time and ram)

Try to do anything with it
(and if it the OS needs a feature let me know)

# Coding Info #

Code
- Apps' (Folder) Programs
  - icon placed on background
  - have their name displayed
  - double click

- SystemPrograms' (Folder) Programs
  - icons at bottom
  - no name
  - single click
  - (should be less of them than apps)

- Reloader
  - refreshes shown apps
  - reloads system settings
  - bottom right
  - double click

- Both
  - Run the main function of the .py
  - def Main(OS): (Has to be this to run on click!)
 
# Movable Frame Class
### Variables:
- root // usually just OS
- icon // is the passed in PIL Image
- frame // This is what you need in order to use movavble frames
- lastMove{X,Y} // unused ints
- mouseDown // bool for drag function
- start_{x,y} // location for frame to spawn
- X // size of frame 'x' wise
- Y // size of frame 'y' wise

### Functions:
- __init__ (tkinter.tk(), PIL Image, [Size for x, Size for y] ) -> object
- self.config_barColor(color as string) -> None

### Internal:
- isDrag(self, event) -> bool // checks if mouse is clicked and held over top of frame
- startdrag(self, event) -> None // executes drag if mouse is still held down
- stopdrag(self, event{unused} ) -> None // makes startdrag() and drag() not possible
- drag(self) -> None // gets original mouse spot to properly calculate the change in location  
