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
        
        for i in range(5):
            self.Units.create(Prey(self.canvas, position=(random.randint(0, 1080), random.randint(0, 720))))
        self.Units.create(Predator(self.canvas, position=(1080, 360)))
        
        for unit in self.Units.unit_list:
            unit.setDestination((random.randint(0, 1080), random.randint(0, 720)))
        self.tk.update()
        
        
    def attackCoolDown(self):
        self.Units.attackCoolDown()
        self.Units.searchCoolDown()
        self.Units.getChild((self.Units.unit_list[0], self.Units.unit_list[1]), self.Units.unit_list[0])
        self.tk.after(1000, self.attackCoolDown)
        
    def stateupdate(self):
        self.Units.delete()
        self.tk.after(10, self.stateupdate)
        
    def mainLoop(self):
        while True:
            self.canvas.delete("all")
            self.Units.search()
            self.Units.setDestination()
            self.Units.move()
            self.tk.update()
            time.sleep(0.005)
   
if __name__ == '__main__':
    g = Game()
    g.attackCoolDown()
    g.stateupdate()
    g.mainLoop()