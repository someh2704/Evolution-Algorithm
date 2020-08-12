from Unit import Unit
import random

class UnitManager:
    def __init__(self, canvas):
        self.canvas = canvas
        self.unit_list = []
    
    def create(self, unit=None):
        if unit == None:
            self.unit_list.append(Unit(self.canvas))
        else:
            self.unit_list.append(unit)
    
    def delete(self):
        for unit in self.unit_list:
            if(unit.status.health < 0):
                unit.state = "DEAD"
                self.canvas.delete(unit.status.uuid)
                self.unit_list.remove(unit)
            elif(unit.status.health <= unit.status.max_health/2):
                unit.status.color = "BLACK"
    
    def attackCoolDown(self):
        for unit in self.unit_list:
            if(unit.status.attack_flag == False):
                unit.status.attack_counter += 1
                if(unit.status.attack_delay <= unit.status.attack_counter):
                    unit.status.attack_flag = True
                    unit.status.attack_counter = 0
    
    def searchCoolDown(self):
        for unit in self.unit_list:
            if(unit.status.search_flag == False):
                if(unit.status.name == "Predator"):
                    print(f"{unit.status.search_delay - unit.status.search_counter}초 남았습니다")
                unit.status.search_counter += 1
                if(unit.status.search_delay <= unit.status.search_counter):
                    unit.status.search_flag = True
                    unit.status.search_counter = 0
    
    def search(self):
        for unit in self.unit_list:
            if(unit.status.search_flag):
                unit.search(self.unit_list)
                unit.status.search_flag = False
    
    def setDestination(self):
        for unit in self.unit_list:
            if(unit.status.name == "Predator"):
                unit.hunt()
            else:
                unit.runAway()

    
    def move(self):
        for unit in self.unit_list:
            unit.move()

