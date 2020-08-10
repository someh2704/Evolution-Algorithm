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
        self.unit_list = [Prey(self.canvas) for i in range(10)]
        self.predator = Predator(self.canvas)
        while True:
            self.canvas.delete("all")
            for unit in self.unit_list:
                unit.runAway(self.predator)
                unit.move()
            self.predator.hunt(self.unit_list)
            self.predator.move()
            
            self.tk.update()
            time.sleep(0.005)
   
g = Game()
g.mainLoop()