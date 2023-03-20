import importlib.util
import tkinter
import os
import sys

def Run(event, OS, File):
    # Parse the module path from the File argument
    module_path = File.split('.')
    module_name = module_path[-1]
    package_path = '.'.join(module_path[:-1])

    # Import the module and run its Main function
    module = importlib.import_module('.' + module_name, package=package_path)
    module.Main()
    
    OS.update()
    # Remove the module from the cache
    del sys.modules['.'.join([package_path, module_name])]

def initSearch(OS,screen):
    print("Does Nothing")