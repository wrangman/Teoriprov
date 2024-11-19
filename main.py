'''
MAIN.PY: this is the main file of licence test app called "Teoriprov" in Swedish

__author__  = "Johan Wrangö"
__version__ = "1.0.0"
__email__   = "johan.wrango@ga.ntig.se"
'''

from questionsManager import QuestionsManager
from window import Window
from testController import TestController
import tkinter as tk

global controller


print("Launching Teoriprov...")

qs = QuestionsManager()  # Create an instance of the Questions class

# Create a root window 
root = tk.Tk()
app = Window(root, qs)  # Create the View

controller = TestController(app, qs)  # Create the Controller

app.initialize()  # Initialize the main loop of the main window


