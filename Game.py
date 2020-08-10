from tkinter import *
from Unit import *
import time
import random

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Evolution Algorithm")
        self.tk.resizable(True, True)
        
        self.canvas = Canvas(self.tk, width=1080, height=720)
        self.canvas.pack()
    
    def mainLoop(self):
        self.unit = Unit(self.canvas)
        while True:
            self.canvas.delete("all")
            self.unit.move()
            self.tk.update()
            time.sleep(0.005)
   
g = Game()
g.mainLoop()