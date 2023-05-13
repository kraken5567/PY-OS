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
    from Window import initScreen, initInfo_Icons, initSystemPrograms, initApps, initReloader
    with open("Sys_Config.json", "r") as config_file:
        config = J.load(config_file)
    
    if config["Fullscreen"]:
        OS.attributes("-fullscreen", config["Fullscreen"])
        OS.geometry("{}x{}+0+0".format(OS.winfo_screenwidth(), OS.winfo_screenheight()))
    else:
        OS.geometry(config["Resolution"])

    # Reestablish everything! :)
    screen.destroy()

    [screen, programbar, Logo, wallpaper] = initScreen(OS)
    core_iconinfo = initInfo_Icons(OS)
    sys_reg = initSystemPrograms(OS, screen, core_iconinfo[0], core_iconinfo[1])
    app_reg = initApps(OS, screen, core_iconinfo[0], core_iconinfo[1])
    reloader_reg = initReloader(OS, screen, programbar, core_iconinfo, sys_reg, app_reg)
    while OS != None:
        OS.update()
        screen = OS.winfo_children()[0]
        wallpaper.update()
        screen.update()