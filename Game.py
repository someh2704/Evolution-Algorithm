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
        self.time = 0
        
        
        # 결과물 확인 용 입니다.
        for i in range(3):
            self.Units.create(Prey(self.canvas, position=(500, 500)))
        
        self.Units.create(Predator(self.canvas, position=(0, 360)))
        
        for unit in self.Units.unit_list:
            unit.setDestination((500, 500))
            
        self.tk.update()
        
        
    def attackCoolDown(self):
        self.Units.attackCoolDown()
        self.Units.searchCoolDown()
        self.Units.birthCoolDown()
        self.tk.after(1000, self.attackCoolDown)
        
    def stateupdate(self):
        self.Units.delete()
        self.tk.after(10, self.stateupdate)
        
    def debugupdate(self):
        print(self.Units.unit_list)
        print(len(self.Units.unit_list))
        self.tk.after(1000, self.debugupdate)
        
    def EVERYTHINGDELETE(self):
        print("Everything Delete")
        for unit in self.Units.unit_list:
            if(unit.info.name == "Prey"):
                self.Units.unit_list.remove(unit)
        self.Units.create(Prey(self.canvas))
        self.Units.create(Prey(self.canvas))
        self.Units.create(Prey(self.canvas))
        
        self.tk.after(20000, self.EVERYTHINGDELETE)
        
    def mainLoop(self):
        while True:
            self.canvas.delete("all")
            self.Units.search()
            self.Units.setDestination()
            self.Units.move()
            self.Units.makeChild()
            self.tk.update()
            time.sleep(0.005)
   
if __name__ == '__main__':
    g = Game()
    g.attackCoolDown()
    g.stateupdate()
    g.debugupdate()
    g.mainLoop()