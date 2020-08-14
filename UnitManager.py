from Unit import *
from Genetic import *
from Status import *
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
            if(unit.status.health <= 0):
                self.unit_list.remove(unit)
                self.canvas.delete(unit.info.uuid)
            elif(unit.status.health <= unit.status.max_health/2):
                unit.info.color = "BLACK"
    
    def attackCoolDown(self):
        for unit in self.unit_list:
            if(unit.info.attack_flag == False):
                unit.info.attack_counter += 1
                if(unit.status.attack_delay <= unit.info.attack_counter):
                    unit.info.attack_flag = True
                    unit.info.attack_counter = 0
    
    def searchCoolDown(self):
        for unit in self.unit_list:
            if(unit.info.search_flag == False):
                unit.info.search_counter += 1
                if(unit.status.search_delay <= unit.info.search_counter):
                    unit.info.search_flag = True
                    unit.info.search_counter = 0
                    
    def birthCoolDown(self):
        for unit in self.unit_list:
            if(unit.info.birth_flag == False):
                unit.info.birth_counter += 1
                if(unit.status.birth_delay <= unit.info.birth_counter):
                    unit.info.birth_flag = True
                    unit.info.birth_counter = 0
    
    def search(self):
        for unit in self.unit_list:
            if(unit.info.search_flag):
                unit.search(self.unit_list)
                unit.info.search_flag = False
    
    def setDestination(self):
        for unit in self.unit_list:
            if(unit.info.name == "Predator"):
                unit.hunt()
            else:
                unit.runAway()
    
    def move(self):
        for unit in self.unit_list:
            unit.move()
    
    def makeChild(self):
        for unit in self.unit_list:
            if(unit.info.birth_flag == True):
                partner = unit.choice()
                if partner != None:
                    
                    self.create(Genetic.breed((unit, partner), Prey(self.canvas)))
                    unit.info.birth_flag = False
                    partner.info.birth_flag = False