from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        """Initialize the Paddle."""
        super().__init__()
        self.color('black')
        self.shape('square')
        self.turtlesize(stretch_len=4, stretch_wid=0.5)
        self.penup()
        self.start_pos()

    def start_pos(self):
        """
        Starting Position for the paddle
        :return:
        """
        self.goto(0,-270)

    def move_right(self):
        self.forward(20)

    def move_left(self):
        self.backward(20)