from turtle import Turtle, Screen
import time
from top_bars import TopBars
from ball import Ball
from paddle import Paddle
from scoring import ScoreBoard


screen=Screen()
screen.title("BreakOut")
screen.bgcolor('#FFF9DE')
screen.setup(width=600, height=600)
screen.tracer(0)

# bars_top = TopBars
# bars_top.create_bars()

# Create Tergets
targets = []
# Starting Positions for the targets
x,y = -280, 150
def create_targets():
    """Create the targets at the top of the screen"""
    global x, y, targets
    for _ in range(4):
        for _ in range(13):
            screen.update()
            target = TopBars(x,y)
            targets.append(target)
            x += 50
        y += 30
        x = -280
create_targets()
def reset():
    """
    Reset the targets to restart the game
    :return:
    """
    global x, y
    for tar in targets:
        tar.goto(1000,1000)
    targets.clear()
    x = -280
    y = 150
    # Call the create function to create the targets again
    create_targets()

ball = Ball()
paddle = Paddle()
scores = ScoreBoard()


# Listen to keystrokes on the Keyboard.
screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)



game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # Test for collision with the targets
    if ball.ycor() > 125:
        for bar in targets:
            # Check for collision between the ball and any of the targets
            # If there is collision the target dissappears and it collided attribute is set to True
            if ball.distance(bar) < 25 and not bar.collided:
                bar.collided = True
                bar.color('#FFF9DE')
                ball.bounce_y()
                scores.point()
    # Check for collision with the Vertical Edges of the Screen
    if ball.xcor() >= 280 or ball.xcor() <= -280:
        ball.bounce_x()
    # Check for collision with the paddle
    if ball.distance(paddle) < 50 and ball.ycor() <= -250:
        ball.bounce_y()
    # Check for collision with the bottom Edge, got to start position and try again.
    if ball.ycor() < -270:
        reset()
        scores.reset_score()
        ball.start_pos()
        paddle.start_pos()
        ball.bounce_y()
    # Check when the ball goes past all the targets and reached the top. The game should end.
    if ball.ycor() >= 300:
        scores.gameover()
        game_on = False
screen.exitonclick()