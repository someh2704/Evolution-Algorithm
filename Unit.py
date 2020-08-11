from Status import *
import math
import random
from tkinter import *
import uuid

class Unit:
    def __init__(self, canvas, position=(10, 10)):
        self.uuid = str(uuid.uuid4()) # 고유 식별자
        self.name = "Unit"
        
        self.state = "stop"
        self.x = position[0] # 현재 좌표
        self.y = position[1]
        self.dx = 0 # 이동할 목표 좌표
        self.dy = 0
        
        self.status = Status()
        self.status.speed = 1
        self.status.size = 20
        
        self.color = "RED"
        self.canvas = canvas
        self.canvas.create_oval(self.x - self.status.size/2, self.y - self.status.size/2,
                                self.x + self.status.size/2, self.y + self.status.size/2, fill=self.color, tags=self.uuid)
        
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
        
        _amount = min(_length, self.status.speed)
        
        self.x += _amount * math.cos(_theta)
        self.y += _amount * math.sin(_theta)
        
        self.canvas.create_oval(self.x - self.status.size/2, self.y - self.status.size/2,
                                self.x + self.status.size/2, self.y + self.status.size/2, fill=self.color, tags=self.uuid)
        
    def getLength(self, position):
        _dx = position[0] - self.x
        _dy = position[1] - self.y
        
        _length = math.sqrt(_dx*_dx + _dy*_dy)
        return _length
    
    def attack(self, unit):
        if(self.status.can_attack):
            unit.status.health -= self.status.damage
            self.status.can_attack = False
        
    
class Predator(Unit):
    def __init__(self, canvas, position=(1080, 720)):
        super().__init__(canvas, position=position)
        self.name = "Predator"
        self.status.health = 100
        self.status.max_health = 100
        self.status.attack_delay = 3
        self.status.speed = 1.5
        self.status.damage = 9
        self.status.range = 10000
        
    def hunt(self, unit_list):
        destination = []
        for unit in unit_list:
            # 자기 자신은 제외
            if(unit.name == self.name):
                continue
            
            _length = self.getLength((unit.x, unit.y))
            
            # 사정거리가 닿으면 공격
            if(_length < self.status.range):
                self.attack(unit)
            
            # 유닛들의 좌표와 나와의 거리를 구하기
            destination.append((unit.x, unit.y, _length))
            
        # 가장 가까운 유닛으로 접근
        target = min(destination, key=lambda info: info[2])
        self.setDestination((target[0], target[1]))
        
class Prey(Unit):
    def __init__(self, canvas, position=(10,10)):
        super().__init__(canvas, position=position)
        self.color = "YELLOW"
        self.name = "Prey"
        self.delay = 0
        self.status.size = 10
        self.status.speed = 2
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