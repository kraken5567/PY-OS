from Window import *

def Main():
    boot_reg = Boot()
    boot_reg[0].mainloop()

def Boot():
    #Start
    OS = initOS()
    [screen,programbar] = initScreen(OS)
    core_iconinfo = initInfo_Icons(OS)
    sys_reg = initSystemPrograms(OS,screen,core_iconinfo[0],core_iconinfo[1])
    app_reg = initApps(OS,screen,core_iconinfo[0],core_iconinfo[1])
    reloader_reg = initReloader(OS,screen,programbar,core_iconinfo,sys_reg,app_reg)
    boot_reg = [OS,screen,programbar,core_iconinfo,sys_reg,app_reg]
    return boot_reg

Main()