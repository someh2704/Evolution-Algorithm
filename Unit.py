from Status import *
from Information import *
from Genetic import *
import math
import random
from tkinter import *

class Unit:
    def __init__(self, canvas, position=(10, 10), file="UnitInfo/UnitInfo.json"):
        
        self.state = "stop"
        self.x = position[0] # 현재 좌표
        self.y = position[1]
        self.dx = 0 # 이동할 목표 좌표
        self.dy = 0
        self.appear_unit = []
        
        self.status = Status(file)
        self.info = Information(file)
        
        self.info.name = "Unit"
        self.info.color = "RED"
        self.canvas = canvas
        self.display()
        
        
    def display(self):
        # 본체 그리기
        self.canvas.create_oval(self.x - self.status.size/2, self.y - self.status.size/2,
                                self.x + self.status.size/2, self.y + self.status.size/2, fill=self.info.color, tags=self.info.uuid)
        # 시야 범위 그리기
        self.canvas.create_oval(self.x - self.status.sight, self.y - self.status.sight,
                                self.x + self.status.sight, self.y + self.status.sight, outline='GREEN', tags=self.info.uuid)
        # 공격 범위 그리기
        self.canvas.create_oval(self.x - self.status.attack_range, self.y - self.status.attack_range,
                                self.x + self.status.attack_range, self.y + self.status.attack_range, outline="BLUE", tags=self.info.uuid)
        
    def setDestination(self, position):
        self.state = "move"
        self.dx = position[0]
        self.dy = position[1]
        
    def move(self):
        if self.state != "move":
            return
        
        _dx = self.dx - self.x
        _dy = self.dy - self.y
        
        _length = math.sqrt(_dx*_dx + _dy*_dy)
        _theta = math.atan2(_dy, _dx)
        
        _amount = min(_length, self.status.walk_speed)
        
        self.x += _amount * math.cos(_theta)
        self.y += _amount * math.sin(_theta)
        
        self.display()
        
    def search(self, unit_list):
        self.appear_unit = []
        for unit in unit_list:
            if(unit.info.name == 'Predator'):
                g = Genetic()
                g.assess(self, self.appear_unit)
            if(unit == self):
                return
            _length = self.getLength((unit.x, unit.y))
            if(_length < self.status.sight):
                self.appear_unit.append(unit)
        
    
    def getLength(self, position):
        _dx = position[0] - self.x
        _dy = position[1] - self.y
        
        _length = math.sqrt(_dx*_dx + _dy*_dy)
        return _length
    
    def attack(self, unit):
        if(self.info.attack_flag):
            _length = self.getLength((unit.x, unit.y))
            if(_length < self.status.attack_range):
                if(unit.status.health <= 0):
                    return
                unit.status.health -= self.status.damage
                print("남은 체력: ", unit.status.health)
                self.info.attack_flag = False
        
    
class Predator(Unit):
    def __init__(self, canvas, position=(1080, 720)):
        super().__init__(canvas, position=position)
        self.info.name = "Predator"
        self.status.size = 20
        self.status.health = 100
        self.status.max_health = 100
        self.status.attack_delay = 2
        self.status.walk_speed = 2
        self.status.sight = 300
        self.status.search_delay = 3
        self.status.damage = 5
        self.status.attack_range = 100
        
    def hunt(self):
        # 주변에 유닛이 없을수도 있으므로 예외처리
        try:
            target = min(self.appear_unit, key=lambda info: self.getLength((info.x, info.y)))
            self.setDestination((target.x, target.y))
            self.attack(target)
        except:
            pass
            
        
class Prey(Unit):
    def __init__(self, canvas, position=(10,10)):
        super().__init__(canvas, position=position)
        self.info.color = "YELLOW"
        self.info.name = "Prey"
        self.delay = 0
        self.status.sight = 5
        self.status.size = 10
        self.status.walk_speed = 1
        self.status.health = 10
        self.status.max_health = 10
        
    def runAway(self):
        if(self.delay < 400):
            self.delay += 1
            return
        
        position = (random.randint(0, 1080), random.randint(0, 720))
        self.setDestination(position)
        self.delay = 0
        
        # _dx = self.x - predator.x
        # _dy = self.y - predator.y
        # _length = math.sqrt(_dx*_dx + _dy*_dy)
        
        # if(_length < 300):
        #     self.setDestination((self.x+_dx, self.y+_dy))
        