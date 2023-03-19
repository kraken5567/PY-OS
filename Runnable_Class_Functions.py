import importlib

class Programs:
    def __init__(self,File,Icon):
        self.File = File
        self.Icon = Icon
    def On_Click(self):
        Program = importlib.import_module(self.File)
        #There should be no parameters needed!
        Program.Main()

class Apps:
    def __init__(self,File,Icon):
        self.File = File
        self.Icon = Icon
    def On_Click(self):
        App = importlib.import_module(self.File)
        #There should be no parameters needed!
        App.Main()