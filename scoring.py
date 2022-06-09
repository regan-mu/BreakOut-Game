from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        """Initialize the ScoreBoard Class."""
        super().__init__()
        self.color('Blue')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the score board each time a you hit the bar."""
        self.clear()
        self.goto(200, 250)
        self.write(f"Score: {self.score}", align='center', font=('Courier', 20, 'normal'))

    def point(self):
        """Player points aggregation"""
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def gameover(self):
        """End Game"""
        self.goto(0, 0)
        self.write(f"You win!", align='center', font=('Courier', 50, 'normal'))