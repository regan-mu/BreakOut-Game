from turtle import Turtle, Screen
import random

class TopBars(Turtle):
    def __init__(self, start_x, start_y):
        """
        Initialize the TopBars Class.
        This class represents the targets at the top of the screen
        """
        super().__init__()
        self.collided = False
        self.start_x = start_x
        self.start_y = start_y
        self.colors = ['green', 'red', 'black', 'maroon', 'purple', 'cyan', 'violet' ]
        self.colr = random.choice(self.colors)
        self.color(self.colr)
        self.shape('square')
        self.turtlesize(stretch_len=2)
        self.penup()
        self.goto(self.start_x,self.start_y)