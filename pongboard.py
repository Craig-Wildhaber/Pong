from turtle import Turtle


class PongBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.l_score = 0
        self.r_score = 0

    def current_score(self):
        self.write(arg=f"{self.l_score}    {self.r_score}", font=("Source Code Pro", 30, "normal"), align="center")

    def update_l_score(self):
        self.l_score += 1

    def update_r_score(self):
        self.r_score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=("Source Code Pro", 20, "normal"), align="center")
