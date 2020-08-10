import math
import random
from tkinter import *

class Unit:
    def __init__(self, canvas, position=(10, 10), size=10, speed=1, color="RED"):
        self.state = "stop"
        self.x = position[0] # 현재 좌표
        self.y = position[1]
        self.dx = 0 # 이동할 목표 좌표
        self.dy = 0
        
        self.size = size
        self.speed = 1
        
        self.color = color
        self.canvas = canvas
        self.canvas.create_oval(self.x - self.size/2, self.y - self.size/2,
                                self.x + self.size/2, self.y + self.size/2, fill=self.color)
        
    def setDestination(self, position):
        self.state = "move"
        self.dx = position[0]
        self.dy = position[1]
        
    def move(self):
        if self.state != "move":
            return
        
        _dx = self.dx - self.x
        _dy = self.dy - self.y
        
        _theta = math.atan2(_dy, _dx)
        _length = math.sqrt(_dx*_dx + _dy*_dy)
        
        _amount = min(_length, self.speed)
        
        self.x += _amount * math.cos(_theta)
        self.y += _amount * math.sin(_theta)
        
        self.canvas.create_oval(self.x - self.size/2, self.y - self.size/2,
                                self.x + self.size/2, self.y + self.size/2, fill=self.color)
        
class Predator(Unit):
    def __init__(self, canvas, position=(1080, 720), size=20, speed=0.5, color='RED'):
        super().__init__(canvas, position=position, size=size, speed=speed, color=color)
        
    def hunt(self, unit_list):
        destination = []
        for unit in unit_list:
            _dx = self.x - unit.x
            _dy = self.y - unit.y
            _length = math.sqrt(_dx*_dx + _dy*_dy)
            
            # 유닛들의 좌표와 나와의 거리를 구하기
            destination.append((unit.x, unit.y, _length))
            
        # 가장 가까운 유닛으로 접근
        target = min(destination, key=lambda info: info[2])
        self.setDestination((target[0], target[1]))
        
class Prey(Unit):
    def __init__(self, canvas, position=(10,10), size=10, speed=1, color="Yellow"):
        super().__init__(canvas, position=position, size=size, speed=speed, color=color)
        self.setDestination((random.randint(0, 1080), random.randint(0, 720)))
    
    def runAway(self, predator):
        # 0.005초에 한번 루프가 돌므로 200번 돌면 3초
        _dx = self.x - predator.x
        _dy = self.y - predator.y
        _length = math.sqrt(_dx*_dx + _dy*_dy)
        
        if(_length < 300):
            self.setDestination((self.x+_dx, self.y+_dy))
        
    