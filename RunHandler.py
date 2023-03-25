import importlib.util
import sys

def Run(event, OS, File):
    # Parse the module path from the File argument
    module_path = File.split('.')
    module_name = module_path[-1]
    package_path = '.'.join(module_path[:-1])

    # Import the module and run its Main function
    module = importlib.import_module('.' + module_name, package=package_path)
    importlib.reload(module)
    module.Main(OS)
    del sys.modules['.'.join([package_path, module_name])]
    OS.update()


def Reload(OS,screen,programbar):
    import json as J
    with open("Sys_Config.json", "r") as C:
        Config = J.load(C)
        if Config["Fullscreen"]:
            OS.attributes("-fullscreen",Config["Fullscreen"])
            OS.geometry(str(OS.winfo_screenwidth()) + "x" + str(OS.winfo_screenheight()))
        else:
            OS.geometry(Config["Resolution"])
        screen.itemconfig(programbar, fill=Config["Taskbar_Color"])
        screen.configure(bg=Config["Wallpaper_Color"])