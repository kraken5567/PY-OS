from Window import *

# Bootloader Here
OS = initOS()
screen = initScreen(OS)

# Any vars needed to globalize
core_iconinfo = initInfo_Icons(OS)

#Icons and programs
sys_reg = initSystemPrograms(OS,screen,core_iconinfo[0],core_iconinfo[1])
app_reg = initApps(OS,screen,core_iconinfo[0],core_iconinfo[1])
Search_Menu = initSearch(OS,screen)
# Looped Functions

# At The End
OS.mainloop()