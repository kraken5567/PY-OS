from WindowsClass import MovableFrame as MF

from PIL import Image
import tkinterweb
import json
import os

def Main(OS):

    ProgDir = "SystemPrograms"
    ProgFolder = "Browser"

    #put icon in frame
    icon = Image.open(f"{ProgDir}\\{ProgFolder}\\{ProgFolder}.png")

    if os.path.isfile(f"{ProgDir}\\{ProgFolder}\\Config.json"):
        with open(f"{ProgDir}\\{ProgFolder}\\Config.json", "r") as config_file:
            config = json.load(config_file)
    

    else:
        with open(f"{ProgDir}\\{ProgFolder}\\Config.json", "w") as config_file:

            default_cfg = {
                "home":         "https://google.com",
                "themeColor":   "white"
                }

            json.dump(default_cfg,config_file)

    PYous = MF(OS, icon, [816, 300]) #816 is the size the window always goes to
    PYous.config_barColor(config["themeColor"])
    PYous.frame.propagate(False)

    Browser = tkinterweb.HtmlFrame(PYous.frame)
    #HTML_label = tkinterweb.HtmlLabel(PYous.frame,text="none")
    
    Browser.load_website(config["home"])
    #[PYous.X, PYous.Y] = [Browser.winfo_width(), Browser.winfo_height()]
    #HTML_label.grid(pady=30)
    Browser.grid(pady=30)
    
    while Browser != None:
        PYous.frame.update()
        #HTML_label.config(text=Browser.resolve_url())