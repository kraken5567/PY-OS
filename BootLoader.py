from Window import *

def Boot(OS):
    #Start
    
    [screen, programbar, Logo, wallpaper] = initScreen(OS)
    core_iconinfo = initInfo_Icons(OS)
    sys_reg = initSystemPrograms(OS, screen, core_iconinfo[0], core_iconinfo[1])
    app_reg = initApps(OS, screen, core_iconinfo[0], core_iconinfo[1])
    reloader_reg = initReloader(OS, screen, programbar, core_iconinfo, sys_reg, app_reg)

    wallpaper.load_gif()

    worked = True

    while OS != None:
        if (worked):
            try:
                OS.update()
                screen.update()
                wallpaper.update()
            except AttributeError:
                worked = False

                OS.update()
                screen.update()
        else:
            OS.update()
            screen = OS.winfo_children()[0]
            screen.update()

    #fix gif
    # - Goes away on reload
    # - Freezes when App/Prog is opened

if __name__ == "__main__":
    OS = initOS()
    Boot(OS)