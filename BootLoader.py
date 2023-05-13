from Window import *

def Boot(OS):
    #Start
    
    [screen, programbar, Logo, wallpaper] = initScreen(OS)
    core_iconinfo = initInfo_Icons(OS)
    sys_reg = initSystemPrograms(OS, screen, core_iconinfo[0], core_iconinfo[1])
    app_reg = initApps(OS, screen, core_iconinfo[0], core_iconinfo[1])
    reloader_reg = initReloader(OS, screen, programbar, core_iconinfo, sys_reg, app_reg)

    while OS != None:
        UpdateOSDisplay(OS, wallpaper)

    #fix gif
    # - Goes away on reload
    # - Freezes when App/Prog is opened

OS = initOS()
Boot(OS)