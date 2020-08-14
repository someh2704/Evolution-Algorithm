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
    def breed(parents, unit, file="UnitInfo/UnitInfo.json"):
        status = Status(file).__dict__
        child = unit
        
        for stat in status:
            _parent1 = parents[0].status.__dict__[stat]
            _parent2 = parents[1].status.__dict__[stat]
            
            if "delay" in stat:
                continue
            child.status.__dict__[stat] = int((_parent1 + _parent2) / random.gauss(2, 0.17))
            
        child.status.health = child.status.max_health
        
        return child
        
if __name__ == "__main__":
    tk = Tk()
    canvas = Canvas(tk, width=1080, height=720)
    a = Predator(canvas)
    b = Predator(canvas)
    
    a.status.health = 585
    b.status.health = 706
    a.status.max_health = 900
    c = Genetic.breed((a, b), Predator(canvas))
    
    print(c.status.attack_range)
    print(c.status.max_health)
    print(c.status.health)
    