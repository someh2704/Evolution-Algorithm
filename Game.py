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
    
    def attackCoolDown(self):
        stime= time.time()
        for unit in self.Units.unit_list:
            if(unit.status.can_attack == False):
                unit.status.delay_count += 1
                if(unit.status.attack_delay < unit.status.delay_count):
                    unit.status.can_attack = True
                    unit.status.delay_count = 0
        etime = time.time()
        next_time = 1000 - int((etime - stime)* 1000)
        self.tk.after(next_time, self.attackCoolDown)
        
    def mainLoop(self):
        for i in range(3):
            self.Units.create(Prey(self.canvas, position=(random.randint(0, 1080), random.randint(0, 720))))
        self.Units.create(Predator(self.canvas, position=(1080, 360)))
        
        
        for unit in self.Units.unit_list:
            unit.setDestination((random.randint(0, 1080), random.randint(0, 720)))
        
        self.tk.update()
        while True:
            stime = time.time()
            self.canvas.delete("all")
            self.Units.setDestination()
            self.Units.move()
            self.Units.delete()
            self.tk.update()
            time.sleep(0.005)
            
   
if __name__ == '__main__':
    g = Game()
    g.attackCoolDown()
    g.mainLoop()