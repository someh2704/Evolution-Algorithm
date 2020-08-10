class Unit:
    def __init__(self, canvas, position=(10, 10), size=10, color="RED"):
        self.state = "stop"
        self.x = position[0] # 현재 좌표
        self.y = position[1]
        self.dx = 0 # 이동할 목표 좌표
        self.dy = 0
        
        self.size = size
        self.speed = 1
        
        self.canvas = canvas
        self.canvas.create_oval(self.x - self.size/2, self.y - self.size/2,
                                self.x + self.size/2, self.y + self.size/2, fill=color)