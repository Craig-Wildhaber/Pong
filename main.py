from turtle import Screen
from paddle import Paddle
from ball import Ball
from pongboard import PongBoard

# Setting up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# Creating objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
pongboard = PongBoard()

# Gives movement keys to the paddles
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
pongboard.current_score()
while game_is_on:
    screen.update()
    # Moves the ball
    ball.move()
    # Detects collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # Detects collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    # Detects point scoring
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.bounce_x()
        pongboard.clear()
        pongboard.update_l_score()
        pongboard.current_score()
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.bounce_x()
        pongboard.clear()
        pongboard.update_r_score()
        pongboard.current_score()
    # Detects game over
    if pongboard.l_score == 10 or pongboard.r_score == 10:
        pongboard.game_over()
        game_is_on = False

screen.exitonclick()
