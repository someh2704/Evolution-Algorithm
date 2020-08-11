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
                self.canvas.delete(unit.uuid)
                self.unit_list.remove(unit)
            elif(unit.status.health <= unit.status.max_health/2):
                unit.color = "BLACK"

    def setDestination(self):
        for unit in self.unit_list:
            if(unit.name == "Predator"):
                unit.hunt(self.unit_list)
            else:
                unit.runAway()

    
    def move(self):
        for unit in self.unit_list:
            unit.move()

