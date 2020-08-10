import math
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
        
        self.canvas.bind_all('<Button-1>', self.setDestination)
        
    def setDestination(self, event: Event):
        self.state = "move"
        self.dx = event.x
        self.dy = event.y
        
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