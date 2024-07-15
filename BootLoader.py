from Window import *

def Boot(OS):
    #Start
    
    [screen, programbar, Logo, wallpaper] = initScreen(OS)
    core_iconinfo = initInfo_Icons(OS)
    sys_reg = initSystemPrograms(OS, screen, core_iconinfo[0], core_iconinfo[1])
    app_reg = initApps(OS, screen, core_iconinfo[0], core_iconinfo[1])
    reloader_reg = initReloader(OS, screen, programbar, core_iconinfo, sys_reg, app_reg)
    
    try:
        wallpaper.load_gif()
        wallpaper.update()
        wallpaperIsColor = False
    except AttributeError:
        wallpaperIsColor = True

    while OS != None:
        if not wallpaperIsColor:
            wallpaper.update()

        OS.update()
        screen.update()

    #fix gif
    # - Freezes when App/Prog is opened

if __name__ == "__main__":
    OS = initOS()
    Boot(OS)