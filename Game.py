from tkinter import *

class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Evolution Algorithm")
        self.tk.resizable(True, True)
        
        self.canvas = Canvas(self.tk, width=1080, height=720)
        self.canvas.pack()
    
    def mainLoop(self):
        while True:
            self.tk.update()
   
g = Game()
g.mainLoop()