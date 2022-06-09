from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        """Initializing the Ball class"""
        super().__init__()
        self.color('blue')
        self.shape('circle')
        self.turtlesize(0.5)
        self.penup()
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.5
        self.start_pos()

    def start_pos(self):
        """
        Set starting Position
        :return:
        """
        self.goto(0, -255)

    def move(self):
        """
        Move forward in the set direction
        :return:
        """
        next_x = self.xcor() + self.x_move
        next_y = self.ycor() + self.y_move
        self.goto(next_x, next_y)

    def bounce_x(self):
        """
        Change direction when the ball hits the vertical edges of the screen
        :return:
        """
        self.x_move *= -1

    def bounce_y(self):
        """
            Change direction when the ball hits the paddle or the top bars
        :return:
        """
        self.y_move *= -1