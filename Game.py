from tkinter import *
from UnitManager import *
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

        self.Units = UnitManager(self.canvas)
        
    def mainLoop(self):
        for i in range(10):
            self.Units.create(Prey(self.canvas))
        self.Units.create(Predator(self.canvas))
        
        for unit in self.Units.unit_list:
            unit.setDestination((400, 400))
        
        self.tk.update()
        while True:
            self.canvas.delete("all")
            self.Units.setDestination()
            self.Units.move()
            self.Units.delete()
            self.tk.update()
            time.sleep(0.005)
   
if __name__ == '__main__':
    g = Game()
    g.mainLoop()