import random
import copy
from Status import *
from Unit import *
from tkinter import *

class Genetic:
    def __init__(self):
        pass
    
    @staticmethod
    def assess(myself, appear_unit):
        table = []
        for unit in appear_unit:
            if(unit.info.name == myself.info.name):
                continue
            
            info = unit.status.__dict__
            info["unit"] = unit
            
            table.append(info)
        return table
    
    @staticmethod
    def breed(parents, child=None, file="UnitInfo/UnitInfo.json"):
        status = Status(file).__dict__
        child = copy.deepcopy(child) if child != None else parents[0] if random.random() < 0.5 else parents[1]
        for stat in status:
            print(stat)
            if(random.random() < 0.5):
                child.status.__dict__[stat] = copy.deepcopy(parents[0].status.__dict__[stat])
            else:
                child.status.__dict__[stat] = copy.deepcopy(parents[1].status.__dict__[stat])
        return child
        
if __name__ == "__main__":
    tk = Tk()
    canvas = Canvas(tk, width=1080, height=720)
    a = Predator(canvas)
    b = Predator(canvas)
    a.status.attack_range = 1000
    
    b.status.attack_range = 2000
    c = Genetic.breed((a, b))
    print("C의 사정거리: ", c.status.attack_range)
    print(c)
    